# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import radio

myRadio = radio.Radio(debug=True)

print(f"connection: {myRadio.check_connection()}")
print(f'address {myRadio.check_address()}')
print(f"network ID {myRadio.check_networkid()}")
print(f"rfband: {myRadio.check_rfband()}")


target_address = None

while True:
    user_input = input()

    myRadio.transmit(target_address, user_input)