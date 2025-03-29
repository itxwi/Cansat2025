# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sensor
import time

current_sensor = sensor.Sensor()

while True:
    time.sleep(.5)
    print(current_sensor.getData())