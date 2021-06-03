# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:47:54 2021

@author: Henock
"""
'''
# python _cropping_gdal.py startdate enddate lat1 lon1 lat1 lon2
# example
# python _cropping_gdal.py  127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907
'''

import os
import sys
os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')

lon1=sys.argv[1]     
lat1=sys.argv[2]     
lon2=sys.argv[3]      
lat2=sys.argv[4]
 


path ="/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Stitched/"  
pathoutput="/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Cropped/" 
if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Cropped")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
         
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907 "+ (path+file) + " "+(pathoutput+file)
        gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te {0} {1} {2} {3} {4} {5} ".format(lon1,lat1,lon2,lat2,(path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te {0} {1} {2} {3} {4} {5} ".format(lon1,lat1,lon2,lat2,(path+file),(file))
        print(gdalscript)
        os.system(gdalscript)
 
    