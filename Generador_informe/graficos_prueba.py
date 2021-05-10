import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


    # DATA FRAME 1
df1 = pd.read_csv('outstats.txt')
df2 = pd.read_excel('Demo_All_VIM_Uni_AlejandroTFG.xlsx')
df3 = pd.read_excel('outstats_i005.txt')

#COJO LA COLUMNA DE VOLUMEN DEL DF1
volumen = df['natvol']
#COJO LAS COLUMNAS DE MEJORÍA ABSOLUTA Y RELATIVA
mejoria_abs = df['Mejoria_Abs_HT']
mejoria_rel = df['Mejoria_Rel_HT']

    # DISEÑO 1
sns.set_context("paper", font_scale=1.4)
plt.xticks(rotation=20)
plt.title("Relación entre el volumen de la lesión y la mejoría clínica")
bplot1 = sns.scatter(data=df1, width=0.5, color="white", linewidth=3)


    # LEYENDA 1
bplot1.set(ylabel='Eje y')

    # guardar boxplot 1
plot_file_name1 = "boxplot1.jpg"
bplot1.figure.savefig(plot_file_name1, format='jpeg',  dpi=200)
bplot1.remove()