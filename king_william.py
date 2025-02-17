# First controller program will display the gyroscope information onto the screen, then sensor information

import Camera,Gyro,Screen,Radio,Sensor
import json
import time

Gyro.calibrateAccel()
Gyro.calibrateGyro()

print(Gyro.getData())
print(Sensor.getData())