import smbus2
import time

class Gyro:
    def __init__(self,ADDR = 0x68):
        #initate
        self.bus = smbus2.SMBus(1)
        self.bus.write_byte_data(ADDR, 0x6B, 0)
        
    