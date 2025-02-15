import time
import board
import adafruit_bme680

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

def setPressure(pressure = 1013.25):
    bme680.sea_level_pressure = pressure

def getData(temp_offset = -5):
    #returns temp, pressure, altitude, gas, huidity
    return bme680.temperature + temp_offset, bme680.pressure,bme680.altitude, bme680.gas,bme680.relative_humidity