import serial
from time import sleep

# Open poort, die daarna te gebruiken is als 'ser':
with serial.Serial('/dev/tty0', 9600, timeout=1) as ser:
    sleep(2)                   # Wacht tot Arduino opnieuw is opgestart.
    for i in range(10):
        data = ser.readline()  # Lees tot aan een nieuwe regel ('\n')
        data = data.decode()   # Zet bytearray om naar een string
        data = data.strip()    # Verwijder nieuw regel ('\n')
        print(f'{i}: {data}')  # Schrijf string naar scherm
