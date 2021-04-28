import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


plt.style.use('seaborn')

df = pd.read_csv("caracteristicas_mejoria2.csv")
#volumen = df['volumen']
centroide_x = df['centroide_x']
mejoria = df['mejoria']

# Ordeno los valores
#x = np.sort(volumen.values.flatten())
#y = np.sort(mejoria.values.flatten())

#plt.scatter(x,y, edgecolor='black',linewidth=1,alpha=0.75)

# Límites de los ejes x e y
#plt.xlim(100, 300)
#plt.ylim(0, 1)

# Establezco las marcas de los ejes x e y
#plt.xticks(range(200,300,10))
#plt.yticks(range(0,100,10))

plt.scatter(centroide_x,mejoria, edgecolor='black',linewidth=1,alpha=0.75)

plt.title("Relación entre el volumen y la mejoría clínica")
plt.xlabel('Mejoría')
plt.ylabel('Volumen')

plt.tight_layout()

plt.show()