# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sensor,gyro
import time

current_sensor = sensor.Sensor()
current_gyro = gyro.Gyro()
print('calibrating')
start = time.monotonic()
current_gyro.calibrate()
print(f'done calibration, time elapsed: {round(time.monotonic(),2)-round(start,2)} seconds')

while True:
    time.sleep(.5)
    print(current_sensor.getData())
    print(current_gyro.get_data())