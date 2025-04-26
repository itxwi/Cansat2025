import matplotlib.pyplot as plt
import helper as h
import math
import time
import os


path = os.path.dirname(os.path.abspath(__file__)) + "\\"

# file structure
# nested dictionaries, first layer's key is time from epoch (eTime)
# 2nd layer's key is time from epoch (again)
#  3rd layer, has 2 possible keys (gyro,sensor), 
# 4th layer - gyro = {x:xVal,y:yVal,z:Val},
# 4th layer -  sensor = {t:temp,p:Pressure,a:Altitude,h:Humidity,g:airResistance}

pp = h.Post_Process()
data = pp.parse_radio('maxwell')

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

def findDirection():
    sumX = sum([g_vals[i][0] for i in range(len(g_vals))])
    sumZ = sum([g_vals[i][2] for i in range(len(g_vals))])
    angle = math.atan2(sumZ, sumX) * 180 / math.pi
    if angle < 0:
        angle += 360
    return angle
def plotGyroXZ():
    x = [times[i] for i in range(len(g_vals))]
    print(x)
    y = [round(math.sqrt(g_vals[i][0]**2 + g_vals[i][2]**2),2) for i in range(len(g_vals))]
    g = Graph("Acceleration (m/s^2)", "Time Elapsed (s)", "Gyro", x, y)
    g.plot()

def plotGyroY():
    x = [times[i] for i in range(len(g_vals))]
    y = [g_vals[i][1] for i in range(len(g_vals))]
    g = Graph("Acceleration (m/s^2)", "Time Elapsed (s)", "Gyro", x, y)
    g.plot()

def plotPara(y,x,name1="goof",name2="goof"):
    if name1 == "goof":
        name1 = x
    if name2 == "goof": 
        name2 = y

    sensorParas = {"t":0,"p":1,"a":2,"h":3,"g":4}
    gyroParas = {"x":0,"y":1,"z":2}


    if x == "time":
        x = [times[i] for i in range(len(sensorVals))]
    elif y == "time":
        y = [times[i] for i in range(len(sensorVals))]


    if y in sensorParas:
        y = [sensorVals[i][sensorParas[y]] for i in range(len(sensorVals))]
    elif y in gyroParas:
        y = [g_vals[i][gyroParas[y]] for i in range(len(g_vals))]
    else:
        raise ValueError("Invalid parameter. Choose from 't', 'p', 'a', 'h', 'g' 9SENSOR) or  'x', 'y', or 'z'. (GYRO)")

    if x in sensorParas:
        x = [sensorVals[i][sensorParas[x]] for i in range(len(sensorVals))]
    elif x in gyroParas:
        x = [g_vals[i][gyroParas[x]] for i in range(len(g_vals))]
    else:
        raise ValueError("Invalid parameter. Choose from 't', 'p', 'a', 'h', 'g' 9SENSOR) or  'x', 'y', or 'z'. (GYRO)")
    g = Graph(f"{name1} vs {name2}", name1, name2, x, y)
    g.plot()
    
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
    g = Graph("Sensor", "Time", "Sensor", x, y)
    g.plot()

plotGyroXZ()
plotGyroY()
plotSensor("a") 
plotPara("p","t")