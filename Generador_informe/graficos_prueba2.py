import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

df = pd.read_csv("caracteristicas_mejoria2.csv")
volumen = df['volumen']
mejoria = df['mejoria']

plt.scatter(mejoria,volumen, edgecolor='black',linewidth=1,alpha=0.75)

plt.title("Relación entre el volumen y la mejoría clínica")
plt.xlabel('Mejoría')
plt.ylabel('Volumen')

plt.tight_layout()

plt.show()