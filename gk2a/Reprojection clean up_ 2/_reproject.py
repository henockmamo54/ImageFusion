# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:00:37 2021

@author: Henock
"""


import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
os.system('export GDAL_NETCDF_BOTTOMUP=NO')

os.environ["GDAL_NETCDF_BOTTOMUP"] = "NO"

path ="/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI004/"  
pathoutput="/bess19/Image_fusion/pre_process/GK2A/projected/VI004/" 
path_ROI ="/bess19/Image_fusion/pre_process/GK2A/ROI/VI004/"  
path_Reprojected ="/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI004/"  

if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/projected/VI004/")
    
if not os.path.exists(path_ROI):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/ROI/VI004/")
    
if not os.path.exists(path_Reprojected):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI004/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
                 
        # add projection
        gdalscript="gdal_translate -a_srs EPSG:4326 -of GTiff "+ (path+file) + " "+(pathoutput+file).replace('.nc','.tif')
        
        print(gdalscript)
        os.system(gdalscript)
        
        #crop smaller target region
        gdalscript="gdal_translate -projwin 123.749492205 40.963868055 129.727693925 35.419980135 -of GTiff "+ (pathoutput+file).replace('.nc','.tif') + " "+(path_ROI+file).replace('.nc','.tif')
        
        print(gdalscript)
        os.system(gdalscript)
        
        # reproject
        gdalscript="gdalwarp -t_srs EPSG:32652 -r near -of GTiff "+ (path_ROI+file).replace('.nc','.tif') + " "+(path_Reprojected+file).replace('.nc','.tif')

        print(gdalscript)
        os.system(gdalscript)

        
 