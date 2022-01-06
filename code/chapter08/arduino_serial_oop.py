import serial
from time import sleep

class Arduino():
    def __init__(self, port, speed):
        # Constructor voor Arduino, open poort:
        self.serial = serial.Serial(port, speed, timeout=.1)
        sleep(2)  # Wacht op reset Arduino
       
    def send_and_read_data(self, data):
        # Stuurt een string en geeft data terug:
        self.serial.write(data.encode())  # Stuur string
        data = self.serial.readline()     # Ontvang data
        return data.decode().strip()      # return data
    
    def __del__(self):
        # Destructor. Sluit poort als object niet meer nodig is
        self.serial.close()