import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


plt.style.use('seaborn')

df = pd.read_csv("caracteristicas_mejoria_americano.csv", sep=";")
df = df.apply(pd.to_numeric)
volumen = df['volumen']
centroide_x = df['centroide_x']
centroide_y = df['centroide_y']
centroide_z = df['centroide_z']
mejoria = df['mejoria']

# Ordeno los valores
x = np.sort(volumen.values.flatten())
y = np.sort(mejoria.values.flatten())

plt.scatter(x,y, edgecolor='black',linewidth=1,alpha=0.75)

# Límites de los ejes x e y
#plt.xlim(100, 300)
plt.ylim(0, 1)

# Establezco las marcas de los ejes x e y
plt.xticks(range(200,300,10))
#plt.yticks(range(0,100,10))

plt.title("Relación entre el volumen de la lesión y la mejoría clínica")
plt.ylabel('Mejoría (%)')
plt.xlabel('Volumen (mm3)')

plt.tight_layout()

plt.savefig('./Graficos/figure1.png')
#plt.show()

#sns.kdeplot(centroide_x,shade=True)
#plt.savefig('./Graficos/figure2.png')
#plt.show()

