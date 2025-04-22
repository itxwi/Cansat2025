# coordinator requisit
print("Cansat booted!")
import sys,os,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import radio,camera,gyro,sensor
import helper

UPDATETIME = .2

"""
The cansat should immedietly begin to
- Log information in unconverted form
- Send information in a converted form
- Take imagery simultaneously
"""

print('initalizing')
ogyro = gyro.Gyro()
ocamera = camera.Camera()
osensor = sensor.Sensor()
oradio = radio.Radio()

enums = helper.Enums()

time.sleep(2)
print('calibrating')
ogyro.calibrate(rounds=1000)
packet = {}
data_gyro=ogyro.get_data()
data_sensor=osensor.get_data()

last_checked = time.time()
while True:
    if time.time()-last_checked>=UPDATETIME:
        last_checked=time.time()
        packet[time.time()] = {}
        oradio.transmit(packet)

