class Dier:
    # Basis beschrijving voor een dier
    naam = ''    # String voor de naam van het dier
    kleur = ''   # String voor de kleur van het dier
    geluid = ''  # String voor het geluid dat het maakt 

    def __init__(self, naam, kleur, geluid):
        # Constructor om een dier-object te maken.
        self.naam = naam
        self.kleur = kleur
        self.geluid = geluid
        
    def maak_geluid(self):
        print(self.geluid + "!")