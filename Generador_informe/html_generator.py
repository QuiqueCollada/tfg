from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
from PIL import Image 

os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 1100.0 --yzoom 1100.0 --zzoom 1100.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile /Users/enrique/GitHubProjects/tfg/4Enrique/ImagenT2.png --voxelLoc 283 260 35 /Users/enrique/GitHubProjects/tfg/4Enrique/T2_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 1.0 1000.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/tfg/4Enrique/Lesion_T2_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')
os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 820.0 --yzoom 820.0 --zzoom 820.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile /Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenT1.png --voxelLoc 110 112 135 /Users/enrique/GitHubProjects/tfg/Img_lesion/T1_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 30.0 450.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/tfg/Img_lesion/Lesion_T1_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')
os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 820.0 --yzoom 820.0 --zzoom 820.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile /Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenSWAN.png --voxelLoc 289 235 61 /Users/enrique/GitHubProjects/tfg/Img_lesion/SWI_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 2.0 2000.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/tfg/Img_lesion/Lesion_SWAN_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')
os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 820.0 --yzoom 820.0 --zzoom 820.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile /Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenFLAIR.png --voxelLoc 289 222 14 /Users/enrique/GitHubProjects/tfg/Img_lesion/SWI_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 20.0 1900.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/tfg/Img_lesion/Lesion_SWAN_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')

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
#im1.show()
imT1cr = imT1.crop((x1, y1, x2, y2))
imT1cr.save("ImagenT1_crop.png")
imSWANcr = imSWAN.crop((x1, y1, x2, y2))
imSWANcr.save("ImagenSWAN_crop.png")
imFLAIRcr = imFLAIR.crop((x1, y1, x2, y2))
imFLAIRcr.save("ImagenFLAIR_crop.png")


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Lesión Paciente X","imagenT2" : "ImagenT2_crop.png", "imagenT1" : "ImagenT1_crop.png", "imagenSWAN" : "ImagenSWAN_crop.png","imagenFLAIR" : "ImagenFLAIR_crop.png","Autor" : "Enrique"}

html_out = template.render(template_vars)
#print(html_out)

Html_file = open("report.html","w")
Html_file.write(html_out)
Html_file.close()

options = {'enable-local-file-access': None}
pdfkit.from_file('report.html', 'report.pdf',options = options)


