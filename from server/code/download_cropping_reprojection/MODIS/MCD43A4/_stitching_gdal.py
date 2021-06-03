# -*- coding: utf-8 -*-
"""
Created on Tue May 11 16:06:20 2021

@author: Henock
"""



 
import os

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/MODIS/MCD43A4/2019" 
OBJECT_NAME = "MOD_Grid_BRDF"
FIELD_NAME = ""
PIXELSIZE = 480.0
pathoutput="/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Stitched/" 
 
if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Stitched/")
 

FIELD_NAMEs=["BRDF_Albedo_Band_Mandatory_Quality_Band1",
"BRDF_Albedo_Band_Mandatory_Quality_Band2",
"BRDF_Albedo_Band_Mandatory_Quality_Band3",
"BRDF_Albedo_Band_Mandatory_Quality_Band4",
"BRDF_Albedo_Band_Mandatory_Quality_Band5",
"BRDF_Albedo_Band_Mandatory_Quality_Band6",
"BRDF_Albedo_Band_Mandatory_Quality_Band7",
"Nadir_Reflectance_Band1",
"Nadir_Reflectance_Band2",
"Nadir_Reflectance_Band3",
"Nadir_Reflectance_Band4",
"Nadir_Reflectance_Band5",
"Nadir_Reflectance_Band6",
"Nadir_Reflectance_Band7"]


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
        oututparameter=" -o " + pathoutput+ datadict[i]["outputfilename"]+"_"+FIELD_NAME+".tif"
        gdalscript="gdal_merge.py "+oututparameter
        
        for filename in datadict[i]["Files"]:
            gdalscript +=' HDF4_EOS:EOS_GRID:"'+filename+'":'+OBJECT_NAME+':'+FIELD_NAME
          
        print(gdalscript,'\n -------- \n')
        
        os.system(gdalscript)
    
    
    
    
    
    
    
    