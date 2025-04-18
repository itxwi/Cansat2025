import radio

myRadio = radio.Radio(debug=True)

print(f"connection: {myRadio.check_connection()}")
print(f'address: {myRadio.check_address()}')
print(f"network ID {myRadio.check_networkid()}")

myRadio.set_band()

print(f"rfband: {myRadio.check_rfband()}")

target_address = None

myRadio.receive()