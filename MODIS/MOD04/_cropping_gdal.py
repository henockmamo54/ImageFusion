# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:47:54 2021

@author: Henock
"""
 
 
import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/MODIS/MOD04/Stitched/"  
# path = "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData/"
pathoutput="/bess19/Image_fusion/download/MODIS/MOD04/Cropped/" 

if not os.path.exists(pathoutput):
    os.makedirs("Cropped")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
        gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907 {0} {1}".format((path+file),(pathoutput+file))
        print(gdalscript)
        os.system(gdalscript)
 
    