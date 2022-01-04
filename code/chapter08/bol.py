from cirkel import Cirkel
from math import pi


class Bol(Cirkel):
    # Klasse genaamd Bol, gebasseerd op Cirkel

    def bereken_inhoud(self):
        # Berekent de inhoud op basis van z'n straal:
        return 4/3 * pi * self.r**3
