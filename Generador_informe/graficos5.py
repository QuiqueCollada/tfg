import matplotlib.pyplot as plt
import pandas as pd

# Cargo los datos del paciente de un fichero csv
dfp = pd.read_csv('/Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/Topography_Report/outstats_sigle_subject.txt')

# Cargo en variables las columnas que deseo comparar
volp = dfp['natvol'].iloc[0]

# Leo los ficheros csv con información del otros pacientes
df1 = pd.read_csv('outstats.txt')
df2 = pd.read_excel('Demo_All_VIM_Uni_AlejandroTFG.xlsx')

# Uso la función merge para generar un único fichero haciendo un "outer join"
fichero_unico = pd.merge(df1, df2,
				on='id',
				how='outer')

fichero_unico.to_excel('fichero_unico.xlsx')

# Cargo el fichero único en un nuevo dataframe
df = pd.read_excel('fichero_unico.xlsx')

# Cargo las características de la lesión que voy a comparar con la mejoría clínica
volumen = df['natvol']

# Cargo las columnas de mejoría clínica (en unidades absolutas y relativas)
mejoria_abs = df['Mejoria_Abs_HT']
mejoria_rel = df['Mejoria_Rel_HT']

# Creo una figura con 2 subplots: uno con la mejoría relativa y otro relacionado con la absoluta
fig = plt.figure(figsize=(14,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.title.set_text('Relación volumen - mejoría clínica relativa')
x = volumen
y = mejoria_rel
ax1.scatter(x,y, edgecolor='black',linewidth=1,alpha=0.75,)
ax1.axvline(x=volp, color = 'red') # Dibujo una línea roja en el dato específico del paciente
ax1.set_ylabel('Mejoría (%)')
ax1.set_xlabel('Volumen (mm3)')

ax2.title.set_text('Relación volumen - mejoría clínica absoluta')
y = mejoria_abs
ax2.scatter(x,y, edgecolor='black',linewidth=1,alpha=0.75,)
ax2.axvline(x=volp, color = 'red')
ax2.set_ylabel('Mejoría')
ax2.set_xlabel('Volumen (mm3)')

# Guardo la figura en una imagen png
plt.savefig('./Graficos/volumen_mejoria.png', dpi=200)

#plt.show()
