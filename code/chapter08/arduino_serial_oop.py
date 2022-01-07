import serial
from time import sleep

class Arduino():
    serial = None  # Poort waarmee gepraat kan worden.

    def __init__(self, port, speed, timeout=.1):
        # Constructor voor Arduino, open poort:
        self.serial = serial.Serial(port, speed, timeout=timeout)
        sleep(2)  # Wacht op reset Arduino

    def send_and_read_data(self, data):
        # Stuurt een string en geeft string terug:
        self.serial.write(data.encode())  # Stuur string
        data = self.serial.readline()     # Ontvang data
        return data.decode().strip()      # return data

    def __del__(self):
        # Destructor. Sluit poort als object niet meer nodig is
        self.serial.close()