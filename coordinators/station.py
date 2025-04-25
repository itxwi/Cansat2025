# coordinator requisit
print("Station Booted!")
import sys,os
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import radio,screen

#Receive example
station_radio = radio.Radio(debug=True)
station_radio.set_address(101)

station_radio.station()