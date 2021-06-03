# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:16:08 2021

@author: Henock
"""

import os

# set parameters for HEG tool 
os.environ['MRTDATADIR']='/bess19/Image_fusion/code/HEGtool/data'
os.environ['LD_LIBRARY_PATH']='/bess19/Image_fusion/code/HEGtool/bin'
os.environ['PGSHOME']='/bess19/Image_fusion/code/HEGtool/TOOLKIT_MTD'
os.environ['HEGUSER']='root'
os.environ['OMP_NUM_THREADS']='1' 

path ="/bess19/Image_fusion/download/MODIS/MOD04/2019" 
pathHeader ="/bess19/Image_fusion/pre_process/MODIS/MOD04/Header"
OBJECT_NAME = "mod04"
FIELD_NAME = "Total_Ozone"
PIXELSIZE = 1000.0
pathoutput="/bess19/Image_fusion/pre_process/MODIS/MOD04/Stitched" 
FIELD_NAMEs=["Deep_Blue_Aerosol_Optical_Depth_550_Land"]

if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/MODIS/MOD04/Stitched")


# group products from the same date
datadict={}
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        filename=os.path.join(root,file)         
        filedata=file.split('.')
        
        if(filedata[1] in datadict.keys()):
            datadict[filedata[1]]["Files"].append(filename)
            datadict[filedata[1]]["ShortFileName"].append(file)
        else:
            datadict[filedata[1]]={"outputfilename": str(filedata[0])+str(filedata[1]), "Files":[filename],"ShortFileName":[file]}
            
def toDict(a):     
    return {i.split("=")[0]:i.split("=")[1] for i in a} 

def getSwathMinMaxLatLonAndPixelSize(files):
    maxlat=[]
    minlat=[]
    maxlong=[]
    minlong=[] 
    pixleXDegrees=""
    pixleYDegrees="" 
    
    for file in files:
        f = open(os.path.join(pathHeader,file.replace('.hdf','.hdr')), "r")
        
        temp=f.read().strip().split('\n')
        v=[i for i in temp if len(i)>0]        
        vals= toDict(v)
        minlat.append(vals["SWATH_LAT_MIN"])
        maxlat.append(vals["SWATH_LAT_MAX"])
        minlong.append(vals["SWATH_LON_MIN"])
        maxlong.append(vals["SWATH_LON_MAX"])
        pixleXDegrees=vals['SWATH_X_PIXEL_RES_DEGREES']
        pixleYDegrees=vals['SWATH_Y_PIXEL_RES_DEGREES'] 
         
    return ["( {0} {1} )".format(max(maxlat), min(minlong)),
            "( {0} {1} )".format(min(minlat), max(maxlong)),
            pixleXDegrees,pixleYDegrees]
         
 
for FIELD_NAME in FIELD_NAMEs:
# prepare the parameter file
    
    for i in datadict:
        originalfileinfo=getSwathMinMaxLatLonAndPixelSize(datadict[i]["ShortFileName"])
        concatfiles='|'.join(map(str,datadict[i]["Files"]))
        parametervalues="""
    NUM_RUNS = 1
    
    BEGIN
    NUMBER_INPUTFILES = {0}
    INPUT_FILENAMES = {1}
    OBJECT_NAME = {2}|
    FIELD_NAME = {3}|
    BAND_NUMBER = 1
    SPATIAL_SUBSET_UL_CORNER = {7}|
    SPATIAL_SUBSET_LR_CORNER = {8}|
    OUTPUT_OBJECT_NAME = {2}|
    OUTGRID_X_PIXELSIZE = {9}
    OUTGRID_Y_PIXELSIZE = {10}
    RESAMPLING_TYPE = NN
    OUTPUT_PROJECTION_TYPE = GEO
    ELLIPSOID_CODE = WGS84
    UTM_ZONE = 52
    OUTPUT_PROJECTION_PARAMETERS = ( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  )
    OUTPUT_FILENAME = {5}/{6}_{3}.tif
    SAVE_STITCHED_FILE = NO
    OUTPUT_STITCHED_FILENAME = D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/TestData/MOD07_L2.A2019222.1320.061.2019223011051_mod07_stitched_.hdf
    OUTPUT_TYPE = GEO
    END
    
    """.format(len(datadict[i]["Files"]),concatfiles,
    OBJECT_NAME,FIELD_NAME,PIXELSIZE,pathoutput,datadict[i]["outputfilename"],
    originalfileinfo[0],originalfileinfo[1],originalfileinfo[2],originalfileinfo[3]) 
       
        with open('param.prm', 'wb') as f:
            f.write(parametervalues.encode('ascii'))
        
        # execute the stitching and cropping
        os.system("/bess19/Image_fusion/code/HEGtool/bin/subset_stitch_swath -p /bess19/Image_fusion/code/download_cropping_reprojection/MODIS/MOD04/param.prm")
            
        
