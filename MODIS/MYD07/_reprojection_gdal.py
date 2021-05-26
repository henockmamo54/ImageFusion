# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:11:36 2021

@author: Henock
"""

import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 

path ="/bess19/Image_fusion/download/MODIS/MYD07/Cropped/"  
# path = "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData/"
pathoutput="/bess19/Image_fusion/download/MODIS/MYD07/Reprojected/" 
 
if not os.path.exists(pathoutput):
    os.makedirs("Reprojected")
 
for root, dirs, files in os.walk(path):
      
    for file in files:
          
        gdalscript="gdalwarp -t_srs EPSG:32652  -r near -tr 1000 1000 {0} {1}".format((path+file),(pathoutput+file))
        print(gdalscript)
        os.system(gdalscript)
 