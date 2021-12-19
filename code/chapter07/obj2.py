import math


class Cirkel:

    def __init__(self, r):
        """
        Deze gekke functie noemen we de constructor.
        Als je een nieuwe instantie van dit object aanmaakt
        met bijv.: x = Cirkel(1)
        Zal deze funtie dus worden aangeroepen met r=1 in dat geval.
        """
        self.r = r  # Deze regel slaat de waarde van r op als classe waarde

    def bereken_oppervlakte(self):
        # Berekent de oppervlakte op basis van de classe waarde r
        opp = math.pi * self.r**2
        return opp

    def bereken_omtrek(self):
        # Berekent de omtrek op basis van de classe waarde r
        omt = math.pi * self.r * 2
        return omt
