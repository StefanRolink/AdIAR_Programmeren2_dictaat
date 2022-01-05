from dier import Dier

class Kat(Dier):
    # Kat-klasse gebasseerd op generiek dier.
    
    def __init__(self, naam, kleur):
        # Roep constructor van superklasse aan, maar met kat-geluid:
        super().__init__(naam, kleur, 'Miauw')
    
    def spin(self):
        print('Purrrrrr...')
        
class Hond(Dier):
    # Honden-klasse gebasseerd op generiek dier.
    
    def __init__(self, naam, kleur):
        # Roep constructor van superklasse aan, maar met hond-geluid:
        super().__init__(naam, kleur, 'Waf woef')
        
    def apport(self):
        print('Bal! Bal! Bal!')
    
class Koe(Dier):
    # Koe-klasse gebasseerd op generiek dier.
    gegeten_gras = 0  # Hoeveelheid gegeten gras
    
    def __init__(self, naam, kleur):
        # Roep constructor van superklasse aan, maar met koe-geluid:
        super().__init__(naam, kleur, 'Mmmmmmboe')
        
    def eet_gras(self):
        self.gegeten_gras += 1  # Eet 1 gras.
        print('Om nom nom')
        
    def geef_melk(self):
        # Geef 1 melk, kost 1 gras.
        if(self.gegeten_gras > 0):
            self.gegeten_gras -= 1
            print('Hier, alsjeblieft: 1 melk!')
        else:
            print('Eerst gras eten..')