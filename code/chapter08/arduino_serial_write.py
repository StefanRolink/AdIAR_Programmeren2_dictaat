import serial
from time import sleep

with serial.Serial('/dev/cu.usbmodem1411401', 9600, timeout=.1) as ser:
    sleep(2)  # Wacht op reset Arduino

    ser.write(b'1')                               # Stuur '1': Led aan
    data = ser.readline()                         # Lees binnengekomen data uit
    print(f'Ontvangen: {data.decode().strip()}')  # Maak data op en print

    sleep(1)  # Even wachten tot Led weer uit moet.

    ser.write('0'.encode())                 # Stuur '0': Led uit
    data = ser.readline().decode().strip()  # Lees data uit en maak op
    print(f'Ontvangen: {data}')             # Print data naar scherm
