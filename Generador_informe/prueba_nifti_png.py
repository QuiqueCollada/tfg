import os
import pandas as pd

# Leo el fichero csv que contiene las coordenadas del centroide de la lesión y lo cargo en un dataframe
df = pd.read_csv('/Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/Topography_Report/outstats_sigle_subject.txt')

# Cargo las coordenadas en variables
xT2 = int(df['cenx_T2'].iloc[0])
print(xT2)
yT2 = int(df['ceny_T2'].iloc[0])
zT2 = int(df['cenz_T2'].iloc[0])

path = "/Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/id023"

# Convertimos con fsleyes las imágenes NIFTI en T1, T2, SWAN y FLAIR a PNG aplicando la máscara de la lesión.
os.system(f'fsleyes render --scene ortho --xcentre  0.00000  0.00000 --ycentre  0.00000  0.00000 --zcentre  0.00000  0.00000 --xzoom 1100.0 --yzoom 1100.0 --zzoom 1100.0 --layout horizontal -hl --performance 3 --movieSync --hideCursor --outfile /Users/enrique/GitHubProjects/tfg/4Enrique/ImagenT2.png --voxelLoc {xT2} {yT2} {zT2} /Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/id023/LesionSegment_New/T2_PO.nii.gz --name "T2_PO.nii.gz" --overlayType volume  --cmap greyscale --displayRange 1.0 1000.0 --cmapResolution 256 --interpolation linear /Users/enrique/GitHubProjects/HIFU_VIM_Topografia_AutoReport/Lesion_Segmentation_Enrique/id023/Rater_Merged/Lesion_T2_PO_1D_W.nii.gz --overlayType mask --maskColour 1.0 0.0 0.0 --outline --interpolation linear')
