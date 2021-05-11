# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:47:54 2021

@author: Henock
"""




 
import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


# path ="/bess19/Image_fusion/download/MODIS/MCD43A4/RC/"  
path = "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData/"
pathoutput="/bess19/Image_fusion/download/MODIS/MCD43A4/Cropped/" 
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
         
        gdalscript="gdalwarp -of GTiff -t_srs EPSG:4326 -te 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907 "+ (path+file) + " "+(pathoutput+file)
        print(gdalscript)
        os.system(gdalscript)
  
# for FIELD_NAME in FIELD_NAMEs:
# # prepare the parameter file
    
#     for i in datadict:
#         oututparameter=" -o " + pathoutput+ datadict[i]["outputfilename"]+"_"+FIELD_NAME+".tif"
#         gdalscript="gdal_merge.py "+oututparameter
        
#         for filename in datadict[i]["Files"]:
#             gdalscript +=' HDF4_EOS:EOS_GRID:"'+filename+'":'+OBJECT_NAME+':'+FIELD_NAME
          
#         print(gdalscript,'\n -------- \n')
        
#         os.system(gdalscript)
    
    
    