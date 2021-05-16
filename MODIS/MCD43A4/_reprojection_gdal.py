# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:11:36 2021

@author: Henock
"""

import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/MODIS/MCD43A4/Cropped/"  
# path = "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData/"
pathoutput="/bess19/Image_fusion/download/MODIS/MCD43A4/Reprojected/" 
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
         
        gdalscript="gdalwarp -t_srs EPSG:32652  -r near -tr 480 480 "+ (path+file) + " "+(pathoutput+file)
        print(gdalscript)
        os.system(gdalscript)
 