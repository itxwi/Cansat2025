import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Gyro,Screen,Radio,Sensor#,Camera
import Helper
import time

dims = ['x','y','z']

cansatOLED = Screen.OLED(fontsize=16)
cansatOLED.clearImage()
cansatOLED.drawFont("calibrating accelerometer",(10,0))
cansatOLED.display()
Gyro.calibrateAccel(delay=0)

cansatOLED.clearImage()
cansatOLED.drawFont("calibrating gyroscope",(10,0))
cansatOLED.display()
Gyro.calibrateGyro(delay=0)

cansatOLED.clearImage()

periods = 0
hertz = .25
gyroState = False #when true we are in sensor mode

while True:
    time.sleep(hertz)
    cansatOLED.clearImage()
    currentLog = Helper.getLog()
    gyroInfo = Gyro.getData()
    sensorInfo = Sensor.getData()

    newInfo = {
        'accel' : gyroInfo['accel'],
        'gyro' : gyroInfo['gyro'],
        'sensor' : sensorInfo
        }


    currentLog[time.time()] = newInfo

    if periods>=7/hertz:
        periods=periods%7/hertz
        gyroState = not gyroState

    #display stuff
    if gyroState:
        cansatOLED.drawFont("accel",(10,0))
        for i,dim in enumerate(dims):
            cansatOLED.drawFont(f"{dim}: {gyroInfo['accel'][dim]}",(10,(i+1)*16))

        cansatOLED.drawFont("gyro",(74,0))
        for i,dim in enumerate(dims):
            cansatOLED.drawFont(f"{dim}: {gyroInfo['gyro'][dim]}",(74,(i+1)*16))
    else:
        cansatOLED.drawFont('Sensor',(10,0))
        for i,reading in enumerate(sensorInfo):
            cansatOLED.drawFont(f"{reading}: {sensorInfo[reading]}",(10,(i+1)*16))

    cansatOLED.display()

    print(newInfo)
    periods+=1
    Helper.writeLog(currentLog)