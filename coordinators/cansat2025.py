# coordinator requisit
print("Cansat booted!")
import sys,os,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import radio,camera,gyro,sensor
import helper
import threading

UPDATETIME = .1

"""
The cansat should immedietly begin to
- Log information in unconverted form ✅
- Send information in a converted form 
- Take imagery simultaneously ✅
"""

#print('initalizing')
ogyro = gyro.Gyro()
ocamera = camera.rpiCam((1000,1000))
osensor = sensor.Sensor()
oradio = radio.Radio(debug=True)

#enums = helper.Enums()
data_manger = helper.DataManager()

#print("modules received")

time.sleep(.5)
#print('calibrating')
ogyro.calibrate(rounds=100)
#print('setting address to 102')
oradio.set_address(102)

def convert_transmitable(packets):
    transmission = ''
    #print(packets)
    for packet in packets:
        for key in packets[packet]:
            transmission+=f'{key}:{packets[packet][key]}~'

    #print(transmission)
    return transmission[0:len(transmission)-1]
        

def cansat_transmit():
    last_checked = time.time()
    while True:
        if time.time()-last_checked>=UPDATETIME:
            data_gyro=ogyro.get_data()
            data_sensor=osensor.get_data()
        
            last_checked=time.time()
            
            packets = {'gyro':data_gyro,'sensor':data_sensor}
            #print("transmitted")
            transmittable = convert_transmitable(packets)
            #print(transmittable)
            data_manger.append_data(last_checked,packets)
            oradio.transmit(transmittable)



def cansat_video():
    x=0
    while True:
        x+=1
        #print(f"taking video {x}")
        ocamera.video(f'test{x}',duration=10)
        #print("video taken")

thread1 = threading.Thread(target=cansat_transmit)
thread2 = threading.Thread(target=cansat_video)

#print('running')
thread1.start()
#print('thread1 begin')
thread2.start()
#print('thread2 begin')