# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:47:54 2021

@author: Henock
"""
 
 
import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/MODIS/MYD04/Stitched/"  
# path ="/bess19/Image_fusion/download/MODIS/MYD04/Cropped1/"  
pathoutput="/bess19/Image_fusion/download/MODIS/MYD04/Cropped/" 

if not os.path.exists(pathoutput):
    os.makedirs("Cropped")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
        gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.2171013894428881 38.1019583730565171 127.3722250533352280 38.2934678769442769 "+ (path+file) + " "+(pathoutput+file)
        # gdalscript="gdalwarp -to SRC_METHOD=NO_GEOTRANSFORM -of GTiff -te 127.2171013894428881 38.1819583730565171 127.3722250533352280 38.2934678769442769 {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 38.18195837298332 127.27222505323994 39.22346787684907 {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.217101389 38.323467877 127.372225053 38.181958373 {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 127.27222505323994 38.18195837298332 38.22346787684907 {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdal_translate -projwin 125.640870434 50.824895844 127.644920487 49.702627814 -of GTiff {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdal_translate -projwin 127.21710138948873 38.22346787684907 127.644920487 49.702627814 -of GTiff {0} {1}".format((path+file),(pathoutput+file))
        # gdalscript="gdal_translate -projwin 127.217101389 38.293467877 127.372225053 38.181958373 -of GTiff {0} {1}".format((path+file),(pathoutput+file))
        print(gdalscript)
        os.system(gdalscript)
 
    