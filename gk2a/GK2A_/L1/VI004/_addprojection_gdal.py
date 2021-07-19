# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:34:28 2021

@author: Henock
"""



import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
os.system('export GDAL_NETCDF_BOTTOMUP=NO')

os.environ["GDAL_NETCDF_BOTTOMUP"] = "NO"

path ="/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI004/"  
pathoutput="/bess19/Image_fusion/pre_process/GK2A/projected/VI004/"  

if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/projected/VI004/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
                 
        gdalscript="gdal_translate -a_srs EPSG:4326 -of GTiff "+ (path+file) + " "+(pathoutput+file).replace('.nc','.tif')
        
        print(gdalscript)
        os.system(gdalscript)
 