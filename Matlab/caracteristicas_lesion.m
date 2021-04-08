clc; close all; clear;

path = ['/Users/enrique/GitHubProjects/tfg/Img_lesion/' 'Lesion_T2_PO_1D_W.nii.gz']
hdr = load_untouch_nii(path);

vol = sum(hdr.vol(:));
hdr.pixdim
prod(hdr.pixdim(1:3)) * vol


