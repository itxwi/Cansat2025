import time
import board
import busio
import adafruit_adxl34x

class Gyro:
    def __init__(self):
        self.axis = ['x', 'y', 'z']
        self.accel_offset = {k: 0 for k in self.axis}

        # Set up I2C and ADXL345
        i2c = busio.I2C(board.SCL, board.SDA)
        self.accel = adafruit_adxl34x.ADXL345(i2c)
        self.accel.address = 0x53  # Just to be explicit

    def get_data(self, place=2, calibrating=False):
        try:
            x, y, z = self.accel.acceleration
            accel_data = dict(zip(self.axis, (x, y, z)))

            if not calibrating:
                for dim in self.axis:
                    accel_data[dim] -= self.accel_offset[dim]

            if place is not None:
                for dim in self.axis:
                    accel_data[dim] = round(accel_data[dim], place)

            return accel_data

        except OSError as e:
            if e.errno == 5:
                print("accelerometer cable disconnected, data lost")
            else:
                raise
        except Exception as e:
            print(f"unexpected error: {e}")

    def calibrate(self, rounds=100, delay=0.01):
        for _ in range(rounds):
            if delay > 0:
                time.sleep(delay)
            data = self.get_data(place=None, calibrating=True)

            for dim in self.axis:
                self.accel_offset[dim] += data[dim]

        self.accel_offset = {
            dim: self.accel_offset[dim] / rounds for dim in self.axis
        }

        print("Done calibration")
        return self.accel_offset

# Example usage:
# accel = Accelerometer()
# accel.calibrate()
# while True:
#     print(accel.get_data())
#     time.sleep(0.5)
