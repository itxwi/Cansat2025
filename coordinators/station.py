# coordinator requisit
print("launched")
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import radio

#Receive example
station_radio = radio.Radio(debug=True)
station_radio.station()