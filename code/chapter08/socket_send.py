import socket

arduino_address = '192.168.1.3'
arduino_port    = 23

with socket.socket() as s:
    s.connect((arduino_address, arduino_port))  # Open connectie
    s.send(b'Hallo vanuit Python!\n')           # Stuur bericht
