from jinja2 import Environment, FileSystemLoader
import pdfkit
from PIL import Image 

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
im_mosaicoT2 = Image.open("/Users/enrique/GitHubProjects/tfg/Img_lesion/mosaicoT2.png")

# Setting the points for cropped image 
x3 = 165
y3 = 0
x4 = 800 - 165
y4 = 600

imMosaicoT2cr = im_mosaicoT2.crop((x3, y3, x4, y4))
imMosaicoT2cr.save("MosaicoT2_crop.png")

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"document_title": "Informe automatizado de topografía de la lesión talámica mediante ultrasonido focal de alta intensidad", "title" : "Lesión Paciente X","imagenT2" : "ImagenT2_crop.png", "imagenT1" : "ImagenT1_crop.png", "imagenSWAN" : "ImagenSWAN_crop.png","imagenFLAIR" : "ImagenFLAIR_crop.png","mosaicoT2" : "MosaicoT2_crop.png","Autor" : "Enrique"}

html_out = template.render(template_vars)
#print(html_out)

Html_file = open("report.html","w")
Html_file.write(html_out)
Html_file.close()

options = {'enable-local-file-access': None}
pdfkit.from_file('report.html', 'report.pdf',options = options)


