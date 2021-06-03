# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:47:54 2021
Edited on 2021-05-28 Juwon Kong

@author: Henock
@ Editor: Juwon Kong
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

xmin=sys.argv[1]     
xmax=sys.argv[2]      
ymin=sys.argv[3]
ymax=sys.argv[4]     


path ="/bess19/Image_fusion/pre_process/Landsat8/Registration"  
pathoutput="/bess19/Image_fusion/pre_process/Landsat8/Cropped/L2" 
if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/Landsat8/Cropped/L2")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
         
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907 "+ (path+file) + " "+(pathoutput+file)
        gdalscript="gdalwarp -of GTiff -t_srs PSG:32652 -te {0} {1} {2} {3} {4} {5} ".format(xmin,ymax,xmax,ymin,(path+file),(pathoutput+file))
        # gdalscript="gdalwarp -of GTiff -t_srs EPSG:32652 -te {0} {1} {2} {3} {4} {5} ".format(lon1,lat1,lon2,lat2,(path+file),(file))
        print(gdalscript)
        os.system(gdalscript)
 
    