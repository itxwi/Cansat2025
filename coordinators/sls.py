# coordinator requisit
import sys,os,time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import radio

#Transmit example

cansat_radio = radio.Radio(debug=True)
lasttransmit = time.time()
counter = 0
while True:
    if time.time()-lasttransmit>1:
        counter+=1
        lasttransmit=time.time()
        cansat_radio.transmit(f'counter: {counter}')