from jinja2 import Environment, FileSystemLoader
import pdfkit
from PIL import Image 
import matplotlib.pyplot as plt
import pandas as pd

# SECCIÓN 1. Procesado y recorte de las imágenes producidas por FSLeyes y ANTs para incluirlas en el informe.

# Opens a image in RGB mode 
imT1 = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenT1.png")
imT2 = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenT2.png")
imSWAN = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenSWAN.png")
imFLAIR = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenFLAIR.png")
  
# Setting the points for cropped image 
x1 = 0
y1 = 140
x2 = 798
y2 = 600 - 130
  
# Cropped image of above dimension 
# (It will not change orginal image) 
imT2cr = imT2.crop((x1, y1, x2, y2))
imT2cr.save("ImagenT2_crop.png")
imT1cr = imT1.crop((x1, y1, x2, y2))
imT1cr.save("ImagenT1_crop.png")
imSWANcr = imSWAN.crop((x1, y1, x2, y2))
imSWANcr.save("ImagenSWAN_crop.png")
imFLAIRcr = imFLAIR.crop((x1, y1, x2, y2))
imFLAIRcr.save("ImagenFLAIR_crop.png")

# Opens a image in RGB mode
im_mosaicoT1 = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/mosaicoT1.png")
im_mosaicoT2 = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/mosaicoT2.png")
im_mosaicoFLAIR = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/mosaicoFLAIR.png")
im_mosaicoSWAN = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/mosaicoSWAN.png")

# Setting the points for cropped image 
x3 = 165
y3 = 0
x4 = 800 - 165
y4 = 600

imMosaicoT1cr = im_mosaicoT1.crop((x3, y3, x4, y4))
imMosaicoT1cr.save("MosaicoT1_crop.png")
imMosaicoT2cr = im_mosaicoT2.crop((x3, y3, x4, y4))
imMosaicoT2cr.save("MosaicoT2_crop.png")
imMosaicoFLAIRcr = im_mosaicoFLAIR.crop((x3, y3, x4, y4))
imMosaicoFLAIRcr.save("MosaicoFLAIR_crop.png")
imMosaicoSWANcr = im_mosaicoSWAN.crop((x3, y3, x4, y4))
imMosaicoSWANcr.save("MosaicoSWAN_crop.png")

# SECCIÓN 2. Inclusión de las características topográficas de la lesión en el informe.

# SECCIÓN 3. Generación de los gráficos para la comparación estadística con una población de pacientes.

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


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"document_title": "Informe automatizado de topografía de la lesión talámica mediante ultrasonido focal de alta intensidad", "title" : "Lesión Paciente X","imagenT2" : "ImagenT2_crop.png", "imagenT1" : "ImagenT1_crop.png", "imagenSWAN" : "ImagenSWAN_crop.png","imagenFLAIR" : "ImagenFLAIR_crop.png","mosaicoT2" : "MosaicoT2_crop.png","mosaicoT1" : "MosaicoT1_crop.png","mosaicoFLAIR" : "MosaicoFLAIR_crop.png","mosaicoSWAN" : "MosaicoSWAN_crop.png","Autor" : "Enrique"}

html_out = template.render(template_vars)
#print(html_out)

Html_file = open("report.html","w")
Html_file.write(html_out)
Html_file.close()

options = {'enable-local-file-access': None}
pdfkit.from_file('report.html', 'report.pdf',options = options)


