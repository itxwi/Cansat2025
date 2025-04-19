# coordinator requisit
print("launched")
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import radio

myRadio = radio.Radio(debug=True)

myRadio.set_address()
myRadio.set_networkid()

print(f"connection: {myRadio.check_connection()}")
print(f'address: {myRadio.check_address()}')
print(f"network ID {myRadio.check_networkid()}")

myRadio.set_band()

print(f"rfband: {myRadio.check_rfband()}")

target_address = None

myRadio.receive()