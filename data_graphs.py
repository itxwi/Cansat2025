import matplotlib.pyplot as plt
import helper as h
import math
import time
import json
import os


path = os.path.dirname(os.path.abspath(__file__)) + "\\"

# file structure
# nested dictionaries, first layer's key is time from epoch (eTime)
# 2nd layer's key is time from epoch (again)
#  3rd layer, has 2 possible keys (gyro,sensor), 
# 4th layer - gyro = {x:xVal,y:yVal,z:Val},
# 4th layer -  sensor = {t:temp,p:Pressure,a:Altitude,h:Humidity,g:airResistance}

pp = h.Post_Process()
with open(os.path.abspath(os.path.join(__file__,'../logs/sdcard.json'))) as file:
    data = json.load(file)





class Graph():
    def __init__(self, title, xLabel, yLabel, xData, yData):
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.xData = xData
        self.yData = yData
    def plot(self):
        plt.plot(self.xData, self.yData)
        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.show()
    def save(self, path):
        self.plot()
        plt.savefig(path + self.title + ".png")
        plt.close()
    
times = list(data.keys())


t_shortened = []
t = times[0]

for num in times:
    num = str(round(float(num)-float(t),2))
    t_shortened.append(num)
lengthened = times
times = t_shortened

g_vals = [[] for _ in times]
sensorVals = [[] for _ in times]
for i,t in enumerate(lengthened):
    gyro = data[t]["gyro"]
    sensor = data[t]["sensor"]
    g_vals[i] = [gyro["x"], gyro["y"], gyro["z"]]
    sensorVals[i] = [sensor["t"], sensor["p"], sensor["a"], sensor["h"], sensor["g"]]

first_altitude = sensorVals[0][2]
for i in range(len(sensorVals)):
    sensorVals[i][2] = sensorVals[i][2] - first_altitude # subtract the first altitude from all altitudes to make it 0 at the start
    sensorVals[i][2] = round(sensorVals[i][2], 2) # round to 2 decimal places

for i in range(len(sensorVals)-9):
    g_vals[i][0] = 0
    g_vals[i][1] = 0
    g_vals[i][2] = 0


def truncate(lastN):
    truncated_times = times[len(times)-lastN:]
    truncated_g_vals = g_vals[len(g_vals)-lastN:]
    truncated_sensorVals = sensorVals[len(sensorVals)-lastN:]
    return truncated_times, truncated_g_vals, truncated_sensorVals

times, g_vals, sensorVals = truncate(lastN=20)
t = times[0]
for i in range(len(times)):
    times[i] = round(float(times[i])-float(t)/10, 2) # round to 2 decimal places

for i in range(len(g_vals)):
    g_vals[i][0] = int(round(g_vals[i][0])) 
    g_vals[i][1] = int(round(g_vals[i][1])) 
    g_vals[i][2] = int(round(g_vals[i][2])) 



def findDirection():
    sumX = sum([g_vals[i][0] for i in range(len(g_vals))])
    sumZ = sum([g_vals[i][2] for i in range(len(g_vals))])
    angle = math.atan2(sumZ, sumX) * 180 / math.pi
    if angle < 0:
        angle += 360
    return angle
def plotGyroSideToSide():
    x = [times[i] for i in range(len(g_vals))]
    y = [round(math.sqrt(g_vals[i][1]**2 + g_vals[i][2]**2),2) for i in range(len(g_vals))]
    g = Graph("Acceleration (m/s^2)", "Time Elapsed (s)", "Gyro", x, y)
    g.plot()
    return g

def plotGyroNet():
    x = [times[i] for i in range(len(g_vals))]
    y = [round(math.sqrt(g_vals[i][0]**2 + g_vals[i][1]**2 + g_vals[i][2]**2),2) for i in range(len(g_vals))]
    g = Graph("Acceleration (m/s^2)", "Time Elapsed (s)", "Gyro", x, y)
    g.plot()
    return g

def findGyroNet():
    return [round(math.sqrt(g_vals[i][0]**2 + g_vals[i][1]**2 + g_vals[i][2]**2),2) for i in range(len(g_vals))]

def plotGyroUpDown():
    x = [times[i] for i in range(len(g_vals))]
    y = [abs(g_vals[i][0]) for i in range(len(g_vals))]
    g = Graph("Acceleration (m/s^2)", "Time Elapsed (s)", "Gyro", x, y)
    g.plot()
    return g

def plotPara(y,x,name1="goof",name2="goof"):
    if name1 == "goof":
        name1 = x
    if name2 == "goof": 
        name2 = y

    sensorParas = {"t":0,"p":1,"a":2,"h":3,"g":4}
    gyroParas = {"x":0,"y":1,"z":2}

    if type(y) != list:
        if y == "time":
            y = [times[i] for i in range(len(sensorVals))]
        elif y in sensorParas:
            y = [sensorVals[i][sensorParas[y]] for i in range(len(sensorVals))]
        elif y in gyroParas:
            y = [g_vals[i][gyroParas[y]] for i in range(len(g_vals))]
        else:
            raise ValueError(f"Wrong data type. for x value. Type is dict or list when yours is {type(y)} ")
    if type(x) != list:
        if x == "time":
            x = [times[i] for i in range(len(sensorVals))]
        elif x in sensorParas:
            x = [sensorVals[i][sensorParas[x]] for i in range(len(sensorVals))]
        elif x in gyroParas:
            x = [g_vals[i][gyroParas[x]] for i in range(len(g_vals))]
        else:
            raise ValueError(f"Wrong data type. for x value. Type is dict or list when yours is {type(x)} ")
    g = Graph(f"{name2} vs {name1}", name1, name2, x, y)
    g.plot()
    return g
    
def plotSensor(parameter):
    if parameter == "t":
        y = [sensorVals[i][0] for i in range(len(sensorVals))]
    elif parameter == "p":
        y = [sensorVals[i][1] for i in range(len(sensorVals))]
    elif parameter == "a":  
        y = [sensorVals[i][2] for i in range(len(sensorVals))]
    elif parameter == "h":
        y = [sensorVals[i][3] for i in range(len(sensorVals))]
    elif parameter == "g":
        y = [sensorVals[i][4] for i in range(len(sensorVals))]
    else:
        raise ValueError("Invalid parameter. Choose from 't', 'p', 'a', 'h', or 'g'.")
    x = [times[i] for i in range(len(sensorVals))]
    g = Graph(f"{parameter} vs Time", "Time", parameter, x, y)
    g.plot()
    return g

def badRiemann(paraVals):
    sums = []
    for i in range(len(paraVals)):
        sums.append(0)
        for j in range(0,i if i != 0 else 1):
            avg = (paraVals[j] + paraVals[j+1])/2
            timeElapsed = times[j+1]-times[j]
            sums[i] += round(avg*timeElapsed)
    return sums

plotPara(badRiemann(findGyroNet()),"time",name2 ="Velocity",name1="Time")
velocityVals = badRiemann(findGyroNet())
plotPara(badRiemann(velocityVals),"time",name2="Displacement",name1="Time")




    

# plotGyroNet()
# plotGyroUpDown()
# plotSensor("a") 
# plotPara("t","p")
plotPara("t","time")
plotPara("p","time")