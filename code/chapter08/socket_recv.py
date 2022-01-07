import socket

arduino_address = '192.168.1.3'
arduino_port    = 23

with socket.socket() as s:
    # Open connectie:
    s.connect((arduino_address, arduino_port))

    # Om de connectie op te zetten, moeten we tenminste iets sturen:
    s.send(b'Ja! Komt u maar')

    # Lees de binnengekomen data als 'bestand':
    with s.makefile() as f:
        for i in range(10):
            # Lees telkens 1 regel en print deze:
            data = f.readline()
            print(f'{i}: {data.strip()}')
