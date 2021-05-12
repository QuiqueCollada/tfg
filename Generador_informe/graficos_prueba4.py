import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Leo los ficheros csv
df1 = pd.read_csv('outstats.txt')
df2 = pd.read_excel('Demo_All_VIM_Uni_AlejandroTFG.xlsx')

# Uso la función merge para generar un único fichero haciendo un "outer join"
fichero_unico = pd.merge(df1, df2,
				on='id',
				how='outer')

fichero_unico.to_excel('fichero_unico.xlsx')

# Cargo el fichero único en un nuevo dataframe
df = pd.read_excel('fichero_unico.xlsx')

#COJO LA COLUMNA DE VOLUMEN DEL DF
volumen = df['natvol']
#COJO LAS COLUMNAS DE MEJORÍA ABSOLUTA Y RELATIVA
mejoria_abs = df['Mejoria_Abs_HT']
mejoria_rel = df['Mejoria_Rel_HT']

    # DISEÑO 1
sns.set_context("paper", font_scale=1.4)
#plt.xticks(rotation=20)
plt.title("Relación entre el volumen de la lesión y la mejoría clínica")
plt.scatter(volumen,mejoria_rel, edgecolor='black',linewidth=1,alpha=0.75)

# Añado etiquetas a los ejes x e y
plt.ylabel('Mejoría (%)')
plt.xlabel('Volumen (mm3)')

plt.savefig('./Graficos/figure1.png')
plt.show()
plt.remove()

