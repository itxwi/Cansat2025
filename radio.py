import time
import serial
import helper

class Radio:
    """
    Network ID (Global group, a bandwidth multiple Addresses can communicate with)
    Address (Local group, unique to each RYRL device in a Network ID) [0~2^16]
    Cansat will utilize Point to Point communications
    Serial buffers utilize bits instead of strings, use b'' strings or encode/decode with UTF-8
    AT COMMAND GUIDE
    https://reyax.com/upload/products_download/download_file/LoRa_AT_Command_RYLR998_RYLR498_EN.pdf
    """
    
    def __init__(self,debug=False,BAUDRATE=115200,filename="radiolog"):
        self.ser = serial.Serial('/dev/ttyS0', baudrate=BAUDRATE)
        self.debug = debug
        self.filename = filename
        
        self.send_at("AT+BAND=905000000")
        self.send_at("AT+NETWORKID=3")
        if debug:
            print("Bandwitdth:" + self.send_at("AT+BAND?"))
            print("Network:" + self.send_at("AT+NETWORKID?"))

    def send_at(self,command, expected_response="OK", timeout=1):
        """
        send any at commands through serial
        """
        self.ser.write((command + "\r\n").encode())
        self.ser.flush()
        response = ""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.ser.in_waiting > 0:
                response += self.ser.read(self.ser.in_waiting).decode()
                if expected_response in response:
                    return response
        return response
    
    def set_address(self,address):
        if self.debug:
            print(self.send_at(f"AT+ADDRESS={address}"))
            return
        self.send_at(f"AT+ADDRESS={address}")


    def recieve(self):
        """
        receiving the transmission
        """
        received_data = ""
        start_time = time.time()
        while time.time() - start_time < 1:
            if self.ser.in_waiting > 0:
                received_data += self.ser.read(self.ser.in_waiting).decode()
                return received_data
            time.sleep(0.1)
        return None

    def station(self,check=.5):
        """
        run this function when you are station
        """
        import screen
        station_screen = screen.OLED()
        data_manager = helper.DataManager()
        print("Receving")
        lastrecieved = time.time()
        while True:
            if time.time()-lastrecieved>check:
                
                lastrecieved=time.time()
                received_message = self.recieve()
                if received_message:
                    
                    # if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                    #     with open(self.filename, "r") as file:
                    #         data = json.load(file)
                    # else:
                    #     data = []
                    # json.dump(data)
                    
                    data_manager.append_data(time.time(),received_message)
                    try:
                        station_screen.clear_image()
                        rssi = received_message.split(',')[4]
                        station_screen.draw_font(rssi,[25,25])
                        station_screen.display()
                    except:
                        pass

                    if self.debug:
                        print(received_message)

    def transmit(self,data):
        """
        pipes to send_at but more legible
        """
        if self.debug:
            print(self.send_at(f"AT+SEND=101,{len(data)},{data}"))
            return
        self.send_at(f"AT+SEND=101,{len(data)},{data}")
"""
#Transmit example

cansat_radio = Radio(debug=True)
lasttransmit = time.time()
counter = 0
while True:
    if time.time()-lasttransmit>1:
        counter+=1
        lasttransmit=time.time()
        cansat_radio.transmit(f'counter: {counter}')
"""

"""
#Receive example
station_radio = Radio(debug=True)
station_radio.station()

"""