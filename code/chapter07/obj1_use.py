from cirkel import Cirkel  # Importeer onze Cirkel definitie.

# Maak een object 'Cirkel' aan met de naam 'my_circle'.
my_circle = Cirkel()

# Roep de functies van Cirkel aan, en sla de waardes op:
omt = my_circle.bereken_omtrek()
opp = my_circle.bereken_oppervlakte()

# Print de waardes:
print(f'Deze cirkel heeft een straal van: {my_circle.r}cm.')
print(f'En daarmee een omtrek van: {omt:.2f}cm.')
print(f'En heeft een oppervlakte van: {opp:.2f}cm^2.')
