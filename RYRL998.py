import serial
import time

class RYLR998:
    def __init__(self,debug=False,BAUDRATE=115200,readTime = .25):
        self.ser = serial.Serial('/dev/serial0', baudrate=BAUDRATE, timeout=1,)
        self.debug = debug              # Enables printing in console
        self.readTime = readTime        # Time waited before reading serial buffer
    
    def check_connection(self):
        # Returns a Boolean based on RYRL998 Status
        self.ser.write(b'AT\r\n')
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if "OK" in response:
            print("Connection is OK.")
            return True
        else:
            print("Connection is not OK.")
            return False

    def check_address(self):
        # Returns the address
        self.ser.write(b'AT+ADDRESS?\r\n')
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response
    
    def send_serial(self,data):
        # Send custom commands
        self.ser.write(f'{data}\r\n'.encode('UTF-8'))
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response
    
    def die(self):
        # dies
        self.ser.close()
        return True
    
    


myRadio = RYLR998(debug=True)
myRadio.check_connection()
myRadio.check_address()

myRadio.send_serial('AT+ADDRESS?')