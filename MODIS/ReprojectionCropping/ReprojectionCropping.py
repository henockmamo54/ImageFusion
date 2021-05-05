
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:09:16 2021

@author: Henock
"""



import os

path ="D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData" 
OBJECT_NAME = "mod07"#"MOD_Grid_BRDF"
FIELD_NAME = "Total_Ozone"
PIXELSIZE = 1000
pathoutput="D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData" #../MCD43A4.A2020238.h27v05.006.2020275001956_MOD_Grid_BRDF_stitched_.hdf


# set parameters for HEG tool
os.system("set MRTDATADIR=c:\HEGtools\HEG_Win\data")
os.system("set LD_LIBRARY_PATH=c:\HEGtools\HEG_Win\bin")
os.system("set MRTBINDIR=c:\HEGtools\HEG_Win\bin")
os.system("set PGSHOME=c:\HEGtools\HEG_Win\TOOLKIT_MTD")
os.system("set HEGUSER=henock")

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
            
            
# prepare the parameter file

for i in datadict:
    # print(i)
    # print(len(datadict[i]["Files"])) 
    
#     parametervalues = """
    
# NUM_RUNS = 1

# BEGIN
# NUMBER_INPUTFILES = 2
# INPUT_FILENAMES = D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData\MOD07_L2.A2019213.1325.061.2019214012332.hdf|D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData\MOD07_L2.A2019213.0220.061.2019213131357.hdf
# OBJECT_NAME = mod07|
# FIELD_NAME = Total_Ozone|
# BAND_NUMBER = 1
# SPATIAL_SUBSET_UL_CORNER = ( 53.559311 109.160179 )
# SPATIAL_SUBSET_LR_CORNER = ( 25.57555 144.677811 )
# OUTPUT_OBJECT_NAME = mod07|
# OUTGRID_X_PIXELSIZE = 0.061983
# OUTGRID_Y_PIXELSIZE = 0.045149
# RESAMPLING_TYPE = NN
# OUTPUT_PROJECTION_TYPE = GEO
# ELLIPSOID_CODE = WGS84
# OUTPUT_PROJECTION_PARAMETERS = ( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  )
# OUTPUT_FILENAME = D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData\MOD07_L2.A2019213.1325.061.2019214012332_mod07.tif
# SAVE_STITCHED_FILE = NO
# OUTPUT_STITCHED_FILENAME = D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData\MOD07_L2.A2019213.1325.061.2019214012332_mod07_stitched_.hdf
# OUTPUT_TYPE = GEO
# END

# """
    concatfiles='|'.join(map(str,datadict[i]["Files"]))
    parametervalues="""
NUM_RUNS = 1

BEGIN
NUMBER_INPUTFILES = {0}
INPUT_FILENAMES = {1}
OBJECT_NAME = {2}|
FIELD_NAME = {3}|
BAND_NUMBER = 1
SPATIAL_SUBSET_UL_CORNER = ( 57.880604 92.037514 )
SPATIAL_SUBSET_LR_CORNER = ( 18.948122 146.763824 )
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
OUTPUT_STITCHED_FILENAME = D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\TestData\MOD07_L2.A2019222.1320.061.2019223011051_mod07_stitched_.hdf
OUTPUT_TYPE = GEO
END

""".format(len(datadict[i]["Files"]),concatfiles,
OBJECT_NAME,FIELD_NAME,PIXELSIZE,pathoutput,datadict[i]["outputfilename"])
#     parametervalues=""" \nNUM_RUNS = 1\n
# BEGIN
# NUMBER_INPUTFILES = {0}
# INPUT_FILENAMES = {1}
# OBJECT_NAME = {2}
# FIELD_NAME = {3}
# BAND_NUMBER = 1
# SPATIAL_SUBSET_UL_CORNER = ( 38.22346787684907 127.21710138948873 )
# SPATIAL_SUBSET_LR_CORNER = ( 38.18195837298332 127.21710138948873 )
# OUTPUT_OBJECT_NAME = MOD_Grid_BRDF
# OUTGRID_X_PIXELSIZE = {4}
# OUTGRID_Y_PIXELSIZE = {4}
# RESAMPLING_TYPE = NN
# OUTPUT_PROJECTION_TYPE = UTM
# ELLIPSOID_CODE = WGS84
# UTM_ZONE = 52
# OUTPUT_PROJECTION_PARAMETERS = ( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0  )
# OUTPUT_FILENAME = {5}/{6}.{3}.tif
# SAVE_STITCHED_FILE = NO
# OUTPUT_STITCHED_FILENAME = {5}
# OUTPUT_TYPE = GEO
# END\n\n
# """.format(len(datadict[i]["Files"]),'|'.join(map(str,datadict[i]["Files"])), 
# OBJECT_NAME,FIELD_NAME,PIXELSIZE,pathoutput,datadict[i]["outputfilename"] )
    
    # # f = open("parameters"+datadict[i]["outputfilename"]+".prm", "w")
    # f = open("test"+i+".t", "w")
    # f.write(parametervalues)
    # f.close() 
    
    with open('heni.t', 'wb') as f:
        f.write(parametervalues.encode('ascii'))
    
    print("///////////////////")
    # print(os.system("echo %MRTDATADIR%"))
        
    # # temp= ("C:\HEGtools\HEG_Win\\bin\subset_stitch_swath -p "+ 
    # #        "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\parameters"+
    # #        datadict[i]["outputfilename"]+".prm")
    # temp= ("C:\HEGtools\HEG_Win\\bin\subset_stitch_swath -p "+ 
    #        "D:\Workplace\githubProjects\ImageFusion\MODIS\ReprojectionCropping\test.prm")
              
    # os.system(temp)
        
