import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("caracteristicas_mejoria2.csv")

#print(df.head())

#plt.figure(figsize=(8,5))
plt.style.use('seaborn')

plt.title("Relación entre el volumen y la mejoría clínica")

volumen = df.volumen
mejoria = df.mejoria
#plt.plot(mejoria, volumen, 'b.')
plt.scatter(mejoria,volumen)

#plt.xlim(0,1)
#plt.ylim(100,500)

#plt.xlabel('Mejoría')
#plt.ylabel('Volumen')

#plt.xticks(df.volumen)

#plt.legend()

plt.show()

#valores = df[["volumen","mejoria"]]
#print(valores)

#ax = valores.plot.bar(x="volumen",y="mejoria",rot=0)
#plt.show()