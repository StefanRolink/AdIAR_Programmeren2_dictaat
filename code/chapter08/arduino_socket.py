import socket

class ArduinoSocket:
    socket  = None
        
    def __init__(self, address, port):
        self.socket = socket.socket()         # Maak socket object aan
        self.socket.connect((address, port))  # Open connectie

    def send(self, msg):
        self.socket.send(msg)
        
    def receive(self, msg='Ja! toe maar'):
        # Om de connectie op te zetten, moeten we tenminste iets sturen:
        self.socket.send(msg.encode())

        # Lees de binnengekomen data als 'bestand':
        with self.socket.makefile() as f:
            data = f.readline()               # Lees 1 regel
            return data.strip()               # en geef deze terug

    def close(self):
        self.socket.close()                   # Sluit connectie