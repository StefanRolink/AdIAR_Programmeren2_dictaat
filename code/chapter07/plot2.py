import matplotlib.pyplot as plt

# Creeer x-waardes:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# y-waardes voor de eerste en tweede meting:
y1 = [2, 3, 4, 5, 1, 2, 3, 4, 7, 1]
y2 = [1, 2, 4, 6, 2, 4, 2, 3, 4, 4]


# Plot de eerste meting:
plt.plot(x, y1, '--',label='eerste meting')

# Plot de tweede meting:
plt.plot(x, y2, '..', label='tweede meting')

# Geef de grafiek labels voor beide assen en een titel:
plt.xlabel('Tijd in minuten')
plt.ylabel('Temperatuur in graden Celcius')
plt.title('Gemeten temperaturen')

# Genereer een legenda (ahv van de ingevoerde labels bij plot()):
plt.legend()

# Laat grafiek zien:
plt.show()
