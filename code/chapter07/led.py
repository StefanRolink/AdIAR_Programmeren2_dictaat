import RPi.GPIO as io

class Led:
    led_pin = 0  # Pin is standaard 0, je kan 'm zetten met de constructor.
    status = False  # De Led staat standaard uit.

    def __init__(self, pin_number, default_state=False):
        # Constructor van Led, geeft led_pin en status een waarde
        # en initieerd de GPIO

        self.led_pin = pin_number
        self.status = default_state

        io.setwarnings(False)  # Onderdruk warnings
        io.setmode(io.BCM)  # Gebruik BCM voor pinaanduiding
        io.setup(self.led_pin, io.OUT)  # Set led_pin als OUTPUT

        # Schrijf de default status naar de led:
        io.output(self.led_pin, self.status)

    def on(self):
        # Zet de led aan!
        io.output(self.led_pin, True)

        # Pas status aan:
        self.status = True

    def off(self):
        # Zet de led uit!
        io.output(self.led_pin, False)

        # Pas status aan:
        self.status = False

    def toggle(self):
        # Toggle led. Zet uit als aan, en andersom.
        self.status = not self.status  # Gooi status om.

        io.output(self.led_pin, self.status)  # Set led.
