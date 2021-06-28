# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:34:28 2021

@author: Henock
"""



import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
os.system('export GDAL_NETCDF_BOTTOMUP=NO')
 


path ="/bess19/Image_fusion/pre_process/GK2A/Cropped/VI008/"  
pathoutput="/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI008/"  

if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI008/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
                 
        gdalscript="gdalwarp -t_srs EPSG:32652 -r near -of GTiff "+ (path+file) + " "+(pathoutput+file)
        
        print(gdalscript)
        os.system(gdalscript)
 