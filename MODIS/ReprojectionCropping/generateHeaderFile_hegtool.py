# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:29:59 2021

@author: Henock
"""
 
import os


# set parameters for HEG tool 
os.environ['MRTDATADIR']='C:/HEGtools/HEG_Win/data'
os.environ['LD_LIBRARY_PATH']='C:/HEGtools/HEG_Win/bin'
os.environ['MRTBINDIR']='C:/HEGtools/HEG_Win/bin'
os.environ['PGSHOME']='C:/HEGtools/HEG_Win/TOOLKIT_MTD'
os.environ['HEGUSER']='henock'


# path ="D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/TestData" 
path="D:\Workplace\githubProjects\ImageFusion\MODIS\DELETE"
OBJECT_NAME = "mod07"
FIELD_NAME = "Total_Ozone"
PIXELSIZE = 1000.0
# pathoutput="D:/Workplace/githubProjects/ImageFusion/MODIS/ReprojectionCropping/Header" 
pathoutput="D:\Workplace\githubProjects\ImageFusion\MODIS\DELETEHEADER"

if not os.path.exists(pathoutput):
    os.makedirs("Header")

FIELD_NAMEs=["Total_Ozone","Water_Vapor"]


# group products from the same date
datadict={}
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        print(os.path.join(path,file))
        os.system("C:/HEGtools/HEG_Win/bin/hegtool -n {0} {1}".format(os.path.join(path,file),os.path.join(pathoutput,file.replace('.hdf','.hdr'))))
            