import matplotlib.pyplot as plt
import pandas as pd

# Cargo los datos del paciente de un fichero csv
dfp = pd.read_csv('/Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/Topography_Report/outstats_sigle_subject.txt')

# Cargo en variables las columnas que deseo comparar
volp = dfp['natvol'].iloc[0]

# Cargo el fichero único en un nuevo dataframe
df = pd.read_excel('fichero_unico.xlsx')

# Cargo las características de la lesión que voy a comparar con la mejoría clínica
volumen = df['natvol']
ataxia = df['Atax_3M']
parestesia = ['Pares_3M']

# Creo una figura con 2 subplots: uno sobre la presencia de ataxia y otro sobre la parestesia
fig = plt.figure(figsize=(14,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.title.set_text('Relación volumen - aparición de ataxia a los 3 meses')
x = ataxia
y = volumen
ax1.boxplot(df)
ax1.axhline(y=volp, color = 'red') # Dibujo una línea roja en el dato específico del paciente
ax1.set_ylabel('Ataxia')
ax1.set_xlabel('Volumen (mm3)')

ax2.title.set_text('Relación volumen - mejoría clínica absoluta')
x = parestesia
ax2.boxplot(y)
ax2.axhline(y=volp, color = 'red')
ax2.set_ylabel('Parestesia')
ax2.set_xlabel('Volumen (mm3)')

# Guardo la figura en una imagen png
#plt.savefig('./Graficos/volumen_ataxia_parestesia.png', dpi=200)

plt.show()
