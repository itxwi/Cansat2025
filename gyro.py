import mpu6050
import time

class Gyro:
    def __init__(self):
        axis = ['x', 'y', 'z']
        self.gyro_offset = {k: 0 for k in axis}
        self.accel_offset = {k: 0 for k in axis}

        self.mpu6050 = mpu6050.mpu6050(0x68)

    def get_data(self, place=2, calibrating=False):
        accel_data = self.mpu6050.get_accel_data()
        gyro_data = self.mpu6050.get_gyro_data()

        if not calibrating:
            for dim in gyro_data:
                gyro_data[dim] -= self.gyro_offset[dim]
            
            for dim in accel_data:
                accel_data[dim] -= self.accel_offset[dim]

        packaged_data = {
            'accel': accel_data,
            'gyro': gyro_data
        }

        if place != None:
            for key in packaged_data:
                for dim in packaged_data[key]:
                    packaged_data[key][dim] = round(packaged_data[key][dim], place)

        return packaged_data

    def calibrate(self, rounds=100, delay=0.01):
        for _ in range(rounds):
            if delay > 0:
                time.sleep(delay)
            data = self.get_data(None, calibrating=True)

            for dim in data['gyro']:
                self.gyro_offset[dim] += data['gyro'][dim]

            for dim in data['accel']:
                self.accel_offset[dim] += data['accel'][dim]

        self.gyro_offset = {key: self.gyro_offset[key] / rounds for key in self.gyro_offset}
        self.accel_offset = {key: self.accel_offset[key] / rounds for key in self.accel_offset}
        print('Done calibration')
        return {
            "gyro_offset": self.gyro_offset,
            "accel_offset": self.accel_offset
        }