# First controller program will display the gyroscope information onto the screen, then sensor information. It will contain the previous values in log.json

import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Gyro,Screen,Radio,Sensor#,Camera
import Helper
import time

Gyro.calibrateAccel()
Gyro.calibrateGyro()
cansatOLED = Screen.OLED()

while True:
    time.sleep(1)
    currentLog = Helper.getLog()
    gyroInfo = Gyro.getData()
    sensorInfo = Sensor.getData()

    newInfo = {
        'accel' : gyroInfo['accel'],
        'gyro' : gyroInfo['gyro'],
        'sensor' : sensorInfo
        }

    currentLog[time.time()] = newInfo
    
    cansatOLED.drawFont("hello world",(0,0))
    cansatOLED.display()

    print(newInfo)
    Helper.writeLog(currentLog)