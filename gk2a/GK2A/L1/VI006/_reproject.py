# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:41:01 2021

@author: Henock
"""
 
'''
example

python3 _reproject.py 38.22346787684907 127.21710138948873 38.18195837298332 127.27222505323994					

'''

import os
import sys

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
os.system('export GDAL_NETCDF_BOTTOMUP=NO')

os.environ["GDAL_NETCDF_BOTTOMUP"] = "NO"

path ="/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI006/"  
pathoutput="/bess19/Image_fusion/pre_process/GK2A/projected/VI006/" 
path_ROI ="/bess19/Image_fusion/pre_process/GK2A/ROI/VI006/"  
path_Reprojected ="/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI006/"  

left_upper_lat= float(sys.argv[1]) 
left_upper_lon= float(sys.argv[2]) 
right_lower_lat=float(sys.argv[3]) 
right_lower_lon=float(sys.argv[4]) 



if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/projected/VI006/")
    
if not os.path.exists(path_ROI):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/ROI/VI006/")
    
if not os.path.exists(path_Reprojected):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/Reprojected/VI006/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
                 
        # add projection
        gdalscript="gdal_translate -a_srs EPSG:4326 -of GTiff "+ (path+file) + " "+(pathoutput+file).replace('.nc','.tif')        
        print(gdalscript)
        os.system(gdalscript)
         
        
        #crop smaller target region
        # gdalscript="gdal_translate -projwin 123.749492205 40.963868055 129.727693925 35.419980135 -of GTiff "+ (pathoutput+file).replace('.nc','.tif') + " "+(path_ROI+file).replace('.nc','.tif')
        gdalscript="gdal_translate -projwin {0} {1} {2} {3} -of GTiff {4} {5}".format(     
        left_upper_lon,left_upper_lat,right_lower_lon,right_lower_lat,(pathoutput+file).replace('.nc','.tif'),(path_ROI+file).replace('.nc','.tif'))        
        print(gdalscript)
        os.system(gdalscript)
        
        # reproject
        gdalscript="gdalwarp -t_srs EPSG:32652 -r near -of GTiff "+ (path_ROI+file).replace('.nc','.tif') + " "+(path_Reprojected+file).replace('.nc','.tif')
        print(gdalscript)
        os.system(gdalscript)

        