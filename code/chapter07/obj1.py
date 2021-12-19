from math import pi


class Cirkel:
    r = 10  # Elke cirkel heeft een straal. In dit geval is r =10

    def bereken_oppervlakte(self):
        # Berekent de oppervlakte op basis van de klasse waarde r
        opp = pi * self.r**2
        return opp

    def bereken_omtrek(self):
        # Berekent de omtrek op basis van de klasse waarde r
        omt = pi * self.r * 2
        return omt
