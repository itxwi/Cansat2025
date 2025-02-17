import smbus2
import time

class Gyro:
    def __init__(self, ADDR=0x68):
        # initiate
        self.ADDR = ADDR
        self.bus = smbus2.SMBus(1)
        self.bus.write_byte_data(self.ADDR, 0x6B, 0)  # Wake up the MPU-6050

    def read_raw_data(self, reg):

        high = self.bus.read_byte_data(self.ADDR, reg)
        low = self.bus.read_byte_data(self.ADDR, reg + 1)
        value = (high << 8) | low
        if value > 32768:
            value = value - 65536
        return value

    def get_gyro_data(self):
        # Read gyroscope data
        gyro_x = self.read_raw_data(0x43)
        gyro_y = self.read_raw_data(0x45)
        gyro_z = self.read_raw_data(0x47)
        return {'x': gyro_x, 'y': gyro_y, 'z': gyro_z}

    def get_accel_data(self):
        # Read accelerometer data
        accel_x = self.read_raw_data(0x3B)
        accel_y = self.read_raw_data(0x3D)
        accel_z = self.read_raw_data(0x3F)
        return {'x': accel_x, 'y': accel_y, 'z': accel_z}


