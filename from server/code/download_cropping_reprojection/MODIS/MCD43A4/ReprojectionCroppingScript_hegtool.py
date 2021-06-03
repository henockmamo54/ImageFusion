# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:15:48 2021

@author: Henock
"""
   
import os


# set parameters for HEG tool 
os.environ['MRTDATADIR']='/bess19/Image_fusion/download/MODIS/HEGtool/data'
os.environ['LD_LIBRARY_PATH']='/bess19/Image_fusion/download/MODIS/HEGtool/bin'
os.environ['PGSHOME']='/bess19/Image_fusion/download/MODIS/HEGtool/TOOLKIT_MTD'
os.environ['HEGUSER']='root'
os.environ['OMP_NUM_THREADS']='1'


path ="/bess19/Image_fusion/download/MODIS/MCD43A4/2019" 
OBJECT_NAME = "MOD_Grid_BRDF"
FIELD_NAME = "Total_Ozone"
PIXELSIZE = 480.0
pathoutput="/bess19/Image_fusion/download/MODIS/MCD43A4/RC" 

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
         
        concatfiles='|'.join(map(str,datadict[i]["Files"]))
        parametervalues="""
    NUM_RUNS = 1
    
    BEGIN
    NUMBER_INPUTFILES = {0}
    INPUT_FILENAMES = {1}
    OBJECT_NAME = {2}|
    FIELD_NAME = {3}|
    BAND_NUMBER = 1
    SPATIAL_SUBSET_UL_CORNER = ( 38.223467877 127.146003864 )|
    SPATIAL_SUBSET_LR_CORNER = ( 38.181958373 127.343397288 )|
    OUTPUT_OBJECT_NAME = {2}|
    OUTGRID_X_PIXELSIZE = {4}
    OUTGRID_Y_PIXELSIZE = {4}
    RESAMPLING_TYPE = NN
    OUTPUT_PROJECTION_TYPE = UTM
    ELLIPSOID_CODE = WGS84
    UTM_ZONE = 52
    OUTPUT_PROJECTION_PARAMETERS = ( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  )
    OUTPUT_FILENAME = {5}/{6}_{3}.tif
    SAVE_STITCHED_FILE = NO
    OUTPUT_TYPE = GEO
    END
    
    """.format(len(datadict[i]["Files"]),concatfiles,
    OBJECT_NAME,FIELD_NAME,PIXELSIZE,pathoutput,datadict[i]["outputfilename"]) 
       
        with open('param.prm', 'wb') as f:
            f.write(parametervalues.encode('ascii'))
        
        # execute the stitching and cropping
        os.system("/bess19/Image_fusion/download/MODIS/HEGtool/bin/subset_stitch_grid -p /bess19/Image_fusion/download/MODIS/MCD43A4/param.prm")
            
        
