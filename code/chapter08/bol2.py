from cirkel import Cirkel
from math import pi


class Bol(Cirkel):
    # Klasse genaamd Bol, gebasseerd op Cirkel

    def bereken_oppervlakte(self):
        # Berekent de oppervlakte op basis van de klasse waarde r
        return 4 * pi * self.r**2
    
    def bereken_inhoud(self):
        # Berekent de inhoud op basis van z'n straal:
        return 4/3 * pi * self.r**3

