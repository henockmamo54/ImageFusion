# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:15:48 2021

@author: Henock
"""
 
 
import os


# set parameters for HEG tool 
os.environ['MRTDATADIR']='C:/HEGtools/HEG_Win/data'
os.environ['LD_LIBRARY_PATH']='C:/HEGtools/HEG_Win/bin'
os.environ['MRTBINDIR']='C:/HEGtools/HEG_Win/bin'
os.environ['PGSHOME']='C:/HEGtools/HEG_Win/TOOLKIT_MTD'
os.environ['HEGUSER']='henock'


path ="D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/TestData" 
OBJECT_NAME = "mod07"
FIELD_NAME = "Total_Ozone"
PIXELSIZE = 1000.0
pathoutput="D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/RC" #../MCD43A4.A2020238.h27v05.006.2020275001956_MOD_Grid_BRDF_stitched_.hdf

FIELD_NAMEs=["Total_Ozone","Water_Vapor"]


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
    SPATIAL_SUBSET_UL_CORNER = ( 38.22346787684907 127.21710138948873 )|
    SPATIAL_SUBSET_LR_CORNER = ( 38.18195837298332 127.27222505323994 )|
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
    OUTPUT_STITCHED_FILENAME = D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/TestData/MOD07_L2.A2019222.1320.061.2019223011051_mod07_stitched_.hdf
    OUTPUT_TYPE = GEO
    END
    
    """.format(len(datadict[i]["Files"]),concatfiles,
    OBJECT_NAME,FIELD_NAME,PIXELSIZE,pathoutput,datadict[i]["outputfilename"]) 
       
        with open('param.prm', 'wb') as f:
            f.write(parametervalues.encode('ascii'))
        
        # execute the stitching and cropping
        os.system("C:/HEGtools/HEG_Win/bin/subset_stitch_swath.exe -p D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/param.prm")
            
        
