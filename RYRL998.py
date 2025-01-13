import serial
import time
import json

class RYLR998:
    # Network ID (Global group, a bandwidth multiple Addresses can communicate with)
    # Address (Local group, unique to each RYRL device in a Network ID) [0~2^16]
    # Cansat will utilize Point to Point communications
    # Serial buffers utilize bits instead of strings, use b'' strings or encode/decode with UTF-8


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
    
    def check_networkid(self):
        # Returns Network ID
        self.ser.write(b'AT+NETWORKID?\r\n')
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response

    def check_rfband(self):
        # Returns RF Band
        self.ser.write(b'AT+BAND?\r\n')
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response
    
    def send_serial(self,data):
        # Send custom commands
        # Encoding and decoding serial monitor in python is not reliable, if possible utilze the other options
        self.ser.write(f'{data}\r\n'.encode('UTF-8'))
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response
    
    def close(self):
        # Closes RYRL998
        self.ser.close()
        return True
    
    def reset(self):
        # Factory Reset
        self.ser.write(b'AT+RESET\r\n')
        time.sleep(self.readTime)
        response = self.ser.read(self.ser.inWaiting()).decode()
        if self.debug:
            print(response)
        return response
    
    def transmit(self,address,data):
        # Transmits data to the address of reciving RYRL998
        # Maxiumum of 240 bytes
    
        self.ser.write(f'AT+SEND={address},{len(data)},{data}\r\n'.encode('UTF-8'))

    
    def receive(self):
        
        global log
        try:
            with open('log.json', "r") as file:
                log = json.load(file)
        except:
            log = {}

        try:
            while True:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode('utf-8').strip()
                    if data:
                        current_time = time.time() # UNIX Timestamp
                        #print(f"[{current_time}] Received data: {data}")

                        log[str(current_time)] = data

                        if data.startswith("+RCV="):
                            parts = data.split(',')
                            node_id, msg_len, message, rssi, snr = parts[0], parts[1], parts[2], parts[3], parts[4]
                            print(f"[{current_time}] Node ID: {node_id}, Message: {message}, RSSI: {rssi}, SNR: {snr}")
                        
                        with open('log.json', "w") as file:
                            json.dump(log, file, indent=4)

                                
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
        except serial.SerialException as e:
            print(f"Serial Error: {e}")
        finally:
            print("Serial monitoring stopped.")

myRadio = RYLR998(debug=True)
myRadio.send_serial('AT+NETWORKID=1')
myRadio.send_serial('AT+ADDRESS=102')

while True:
    newMessage = input()
    myRadio.transmit(101, newMessage)