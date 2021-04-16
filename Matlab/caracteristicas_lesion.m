clc; close all; clear;

path = ['/Users/enrique/GitHubProjects/tfg/Img_lesion/' 'Lesion_T2_PO_1D_W.nii.gz']
hdr = load_nifti(path);

vol = sum(hdr.vol(:));
hdr.pixdim
prod(hdr.pixdim(2:4)) * vol

BW = imread('/Users/enrique/GitHubProjects/tfg/Img_lesion/ImagenT2.png');

s = regionprops(BW,'centroid');
centroids = cat(1,s.Centroid);

s = regionprops(BW,'boundingbox');
boundingbox = cat(1,s.BoundingBox);