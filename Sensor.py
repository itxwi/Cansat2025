import time
import board
import adafruit_bme680

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

def setPressure(pressure = 1013.25):
    bme680.sea_level_pressure = pressure

def getData(temp_offset = -5, place=2):

    """
    {
        "temp": bme680.temperature + temp_offset,
        "pressure": bme680.pressure,
        "altitude":bme680.altitude,
        "gas": bme680.gas,
        "humidity":bme680.relative_humidity}
    """

    if place:

        return {
            "temp": round(bme680.temperature + temp_offset,place),
            "pressure": round(bme680.pressure,place),
            "altitude":round(bme680.altitude,place),
            "gas": round(bme680.gas,place),
            "humidity":round(bme680.relative_humidity,place)
        }
    else:
        return {
        "temp": bme680.temperature + temp_offset,
        "pressure": bme680.pressure,
        "altitude":bme680.altitude,
        "gas": bme680.gas,
        "humidity":bme680.relative_humidity}