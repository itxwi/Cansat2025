import mpu6050
import time

mpu6050 = mpu6050.mpu6050(0x68) # Address for MPU6050 is usually 0x68

gyrooffset = {'x': 0, 'y': 0, 'z': 0}
acceloffset = {'x': 0, 'y': 0, 'z': 0}

def getData(place=2,calibrating = False):
    """

    "accel": accelerometer_data,
    "gyro": gyroscope_data

    """
    # round = decimal place
    accelerometer_data = mpu6050.get_accel_data()
    gyroscope_data = mpu6050.get_gyro_data()
    # temperature = mpu6050.get_temp()

    # Apply offsets, when calibrating ensure the object is not in motion
    if not calibrating:
        for dim in gyroscope_data:
            gyroscope_data[dim] -= gyrooffset[dim]

        for dim in acceloffset:
            accelerometer_data[dim] -=acceloffset[dim]

    if place is None:
        return {"accel": accelerometer_data,
                "gyro": gyroscope_data}
                #"temp": temperature}
    else:
        return {"accel": {dim: round(accelerometer_data[dim], place) for dim in accelerometer_data},
                "gyro": {dim: round(gyroscope_data[dim], place) for dim in gyroscope_data}}
                #"temp": round(temperature, place)}

def calibrateGyro(rounds=100,delay = .01):
    global gyrooffset
    for _ in range(rounds):
        if delay>0:
            time.sleep(delay)
        data = getData(None,calibrating=True)
        for dim in data['gyro']:
            gyrooffset[dim] += data['gyro'][dim]
    gyrooffset = {key: gyrooffset[key] / rounds for key in gyrooffset}

    print('done gyroscope calibration')
    return gyrooffset

def calibrateAccel(rounds=100, delay =.01):
    global acceloffset
    for _ in range(rounds):
        if delay>0:
            time.sleep(delay)
        data = getData(None,calibrating=True)
        for dim in data['accel']:
            acceloffset[dim] += data['accel'][dim]
    acceloffset = {key: acceloffset[key] / rounds for key in acceloffset}

    print('done accelerometer calibration')
    return acceloffset