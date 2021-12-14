import matplotlib.pyplot as plt
import numpy as np

# Genereer x-waardes, van -pi tot pi, met stapjes van 0.1:
x = np.arange(-np.pi, np.pi, 0.1)

# Bereken y-waardes door sinus uit te rekenen voor alle x-waardes:
y = np.sin(x)

# Plot de sinus en laat grafiek zien:
plt.plot(x, y)
plt.show()
