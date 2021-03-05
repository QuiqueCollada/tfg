from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 1100.0 --yzoom 1100.0 --zzoom 1100.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile ImagenT2.png --voxelLoc 283 260 35 /Users/enrique/GitHubProjects/tfg/4Enrique/T2_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 1.0 1000.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/tfg/4Enrique/Lesion_T2_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Lesión en T2 - Paciente X","imagen" : "ImagenT2.png","leyenda" : "Lesión talámica","Autor" : "Enrique"}

html_out = template.render(template_vars)
#print(html_out)

Html_file = open("report.html","w")
Html_file.write(html_out)
Html_file.close()

options = {'enable-local-file-access': None}
pdfkit.from_file('report.html', 'report.pdf',options = options)


