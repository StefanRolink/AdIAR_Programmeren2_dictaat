import socket

arduino_address = '192.168.1.113'
arduino_port    = 23

s = socket.socket()
s.connect((arduino_address, arduino_port))

s.send(b'Hallo vanuit Python!\n')
s.close()