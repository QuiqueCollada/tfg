import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

#data = np.genfromtxt("caracteristicas_mejoria5.csv", delimiter=",", names=["paciente", "volumen","mejoria"])
path = "caracteristicas_mejoria5.csv"
data = np.genfromtxt(path, delimiter=',', encoding='utf8', dtype=str, names=True)
print(data)
print(data['paciente'])
#plt.plot(data['volumen'], data['mejoria'])
#plt.xlim(100, 300)
#plt.ylim(0, 100)
#plt.show()
