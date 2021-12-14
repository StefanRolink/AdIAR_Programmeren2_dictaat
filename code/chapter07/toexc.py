import pandas as pd

# Gegeven enkele x en y waardes:
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 3, 4, 5, 2, 3, 4, 5, 2, 3]

# 'zip' de beide lijsten in elkaar:
data = zip(x, y)

# Maak een data-frame aan op basis van data, en geef de kolommen een naam:
df = pd.DataFrame(data, columns=['Tijdstip', 'Waardes'])

# Definieer writer, met bestandsnaam en bestandstype:
writer = pd.ExcelWriter('test.xlsx')

# Verwerk de data-frame als excel-structuur:
df.to_excel(writer, index=False)

# Sla de excel-structuur op als daadwerklijk excel-bestand:
writer.save()
