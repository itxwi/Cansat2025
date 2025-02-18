import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Gyro,Screen,Radio,Sensor#,Camera
import Helper
import time

dims = ['x','y','z']

Gyro.calibrateAccel(delay=0)
Gyro.calibrateGyro(delay=0)
cansatOLED = Screen.OLED(fontsize=7)

while True:
    time.sleep(.5)
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
    for i,dim in enumerate(dims):
        cansatOLED.drawFont(f"{dim}: {gyroInfo['accel'][dim]}",(0,i*6))
    
    cansatOLED.display()

    print(newInfo)
    Helper.writeLog(currentLog)