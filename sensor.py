import board
import adafruit_bme680


class Sensor:
    def __init__(self,sea_level = 1013.25):
        i2c = board.I2C()
        self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
        self.bme680.sea_level_pressure = sea_level
    

    def set_pressure(self, pressure = 1013.25):
        self.bme680.sea_level_pressure = pressure

    def get_data(self,temp_offset = -5, place=2):

        """
        {
            "temp": bme680.temperature + temp_offset,
            "pressure": bme680.pressure,
            "altitude":bme680.altitude,
            "gas": bme680.gas,
            "humidity":bme680.relative_humidity}
        """
        try:
            data = {
                "t": self.bme680.temperature + temp_offset,
                "p": self.bme680.pressure,
                "a":self.bme680.altitude,
                "g": self.bme680.gas,
                "h":self.bme680.relative_humidity
                }

            if place:
                return {
                    k:round(v,place) for k,v in data.items()
                }
            else:
                return data
        except OSError as e:
            if e.errno == 5:
                print("sensor cable disconnected, data lost")
            else:
                raise  # Re-raise other OSErrors
        except Exception as e:
            print(f"unexpected error: {e}")