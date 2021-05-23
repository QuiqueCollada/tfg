# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
  
# Cargo los datos del paciente de un fichero csv
dfp = pd.read_csv('/Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/Topography_Report/outstats_sigle_subject.txt')

# Cargo en variables las columnas que deseo comparar
volp = dfp['natvol'].iloc[0]

# Cargo el fichero único en un nuevo dataframe
df = pd.read_excel('fichero_unico.xlsx')

df_atax = df[(df['Atax_3M'] == 1)] # Filtro por aquellos que tienen Ataxia
vol_atax = df_atax['natvol'].dropna()  # Extraigo el volumen de aquellos que tienen ataxia y elimino los valores NaN        

df_natax = df[(df['Atax_3M'] == 0)] # Filtro por aquellos que NO tienen Ataxia
vol_natax = df_natax['natvol'].dropna()

df_pares = df[(df['Pares_3M'] == 1)] # Filtro por aquellos que tienen Ataxia
vol_pares = df_atax['natvol'].dropna()  # Extraigo el volumen de aquellos que tienen ataxia y elimino los valores NaN        

df_npares = df[(df['Pares_3M'] == 0)] # Filtro por aquellos que NO tienen Ataxia
vol_npares = df_natax['natvol'].dropna()

vol_ap = [vol_natax,vol_atax,vol_npares,vol_pares]
  
fig = plt.figure(figsize =(10, 7))
plt.boxplot(vol_ap)
plt.title("Relación entre el volumen de la lesión y la aparición de ataxia y parestesia")
plt.ylabel('Volumen (mm3)')
plt.axhline(y=volp, color = 'red')
plt.xticks([1, 2, 3, 4], ['Sin ataxia', 'Con ataxia', 'Sin parestesia', 'Con parestesia'])

plt.savefig('./Graficos/volumen_ataxia_parestesia.png', dpi=200)
  
# show plot
#plt.show()