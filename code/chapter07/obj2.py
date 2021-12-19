from math import pi


class Cirkel:
    r = 0  # De straal is standaard 0, je kan 'm zetten met de constructor.

    def __init__(self, r):
        # Deze gekke functie is dus de constructor.
        self.r = r  # Deze regel slaat de waarde van r op als classe waarde

    def bereken_oppervlakte(self):
        # Berekent de oppervlakte op basis van de klasse waarde r
        return pi * self.r**2

    def bereken_omtrek(self):
        # Berekent de omtrek op basis van de klasse waarde r
        return pi * self.r * 2
