# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:06:20 2021

@author: Henock
"""
 
import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/MODIS/MOD04/2019" 
OBJECT_NAME = "mod04"
FIELD_NAME = ""
PIXELSIZE = 480.0
pathoutput="/bess19/Image_fusion/download/MODIS/MOD04/Stitched/" 

FIELD_NAMEs=["Deep_Blue_Aerosol_Optical_Depth_550_Land"]


# group products from the same date
datadict={}
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        filename=os.path.join(root,file)         
        filedata=file.split('.')
        
        if(filedata[1] in datadict.keys()):
            datadict[filedata[1]]["Files"].append(filename)
        else:
            datadict[filedata[1]]={"outputfilename": str(filedata[0])+str(filedata[1]), "Files":[filename]}
            
  
for FIELD_NAME in FIELD_NAMEs:
# prepare the parameter file
    
    for i in datadict: 
        oututparameter=" -o {0}{1}_{2}.tif".format(pathoutput, datadict[i]["outputfilename"],FIELD_NAME)
        gdalscript="gdal_merge.py "+oututparameter
        
        for filename in datadict[i]["Files"]: 
            gdalscript +=' HDF4_EOS:EOS_SWATH:"{0}":{1}:{2}'.format(filename,OBJECT_NAME,FIELD_NAME)
          
        print(gdalscript,'\n -------- \n')
        
        os.system(gdalscript)
    