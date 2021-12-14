import pandas as pd
import matplotlib.pyplot as plt

# Lees spreadsheet in:
df = pd.read_excel('excel1.xlsx')

# Laad de x en y waardes in op basis van kolomdata:
x = df['Tijdstip']
y = df['Waarde']

# Extra's: Laat een grid zien op de achtergrond:
plt.grid()

# Set x en y-label:
plt.xlabel('Tijdstip')
plt.ylabel('Waarde')

# Plot en print grafiek:
plt.plot(x, y)
plt.show()
