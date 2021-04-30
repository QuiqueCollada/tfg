import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('caracteristicas_mejoria6.csv')

df['volumen'] = df['volumen'].str.replace(',', '.').astype(float)
df['mejoria'] = df['mejoria'].str.replace(',', '.').replace('%','',regex=True).astype(float)
df.apply(pd.to_numeric)
print(df)

x = df["volumen"]
print(x)
y = df["mejoria"]

plt.scatter(x,y)
plt.show()