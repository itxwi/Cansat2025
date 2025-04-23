# coordinator requisit
print("Cansat booted!")
import sys,os,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import radio,camera,gyro,sensor
import helper
import threading

UPDATETIME = .2

"""
The cansat should immedietly begin to
- Log information in unconverted form
- Send information in a converted form
- Take imagery simultaneously
"""

print('initalizing')
ogyro = gyro.Gyro()
ocamera = camera.rpiCam((1000,1000))
osensor = sensor.Sensor()
oradio = radio.Radio()

#enums = helper.Enums()
data_manger = helper.DataManager()

print("modules received")

time.sleep(2)
print('calibrating')
ogyro.calibrate(rounds=1000)

def cansat_transmit():
    packet = {}
    data_gyro=ogyro.get_data()
    data_sensor=osensor.get_data()

    last_checked = time.time()
    while True:
        if time.time()-last_checked>=UPDATETIME:
            last_checked=time.time()
            packet[time.time()] = {'gyro':data_gyro,'sensor':data_sensor}
            
            data_manger.append_data()

            oradio.transmit(packet)
            

def cansat_video():
    x=0
    while True:
        x+=1
        print(f"taking video {x}")
        ocamera.video(f'test{x}',duration=10)
        print("video taken")

thread1 = threading.Thread(target=cansat_transmit)
thread2 = threading.Thread(target=cansat_video)

thread1.start()
thread2.start()