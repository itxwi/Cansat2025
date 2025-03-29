import board
import adafruit_bme680


class Sensor:
    def __init__(self,sea_level = 1013.25):
        i2c = board.I2C()
        self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
        self.bme680.sea_level_pressure = sea_level
    

    def setPressure(self, pressure = 1013.25):
        self.bme680.sea_level_pressure = pressure

    def getData(self,temp_offset = -5, place=2):

        """
        {
            "temp": bme680.temperature + temp_offset,
            "pressure": bme680.pressure,
            "altitude":bme680.altitude,
            "gas": bme680.gas,
            "humidity":bme680.relative_humidity}
        """

        data = {
            "temp": self.bme680.temperature + temp_offset,
            "pressure": self.bme680.pressure,
            "altitude":self.bme680.altitude,
            "gas": self.bme680.gas,
            "humidity":self.bme680.relative_humidity
            }

        if place:
            return {
                k:round(v,place) for k,v in data.items()
            }
        else:
            return data