import pandas as pd

# Lees spreadsheet in:
df = pd.read_excel('excel1.xlsx')

# Schrijf alle gevonden kolommen naar het scherm:
for name in df.columns:
    print(name)
