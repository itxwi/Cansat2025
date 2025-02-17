# First controller program will display the gyroscope information onto the screen, then sensor information. It will contain the previous values in log.json

import Gyro,Screen,Radio,Sensor#,Camera
import Helper
import time

Gyro.calibrateAccel()
Gyro.calibrateGyro()
cansatOLED = Screen.OLED()

while True:
    time.sleep(.1)
    currentLog = Helper.getLog()
    currentInfo = Gyro.getData()

    currentLog[time.time()] = currentInfo
    
    cansatOLED.drawFont("hello world",(0,0))

    Helper.writeLog(currentLog)