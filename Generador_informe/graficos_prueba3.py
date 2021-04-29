import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("caracteristicas_mejoria3.csv")

print(df)

df.plot(kind = 'scatter', x = 'volumen', y = 'mejoria')

x = df.volumen
y = df.mejoria

#plt.scatter(x,y)

plt.title("Relación entre el volumen y la mejoría clínica")

plt.show()