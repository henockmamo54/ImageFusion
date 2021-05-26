# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:29:59 2021

@author: Henock
"""
 
import os

# set parameters for HEG tool 
os.environ['MRTDATADIR']='/bess19/Image_fusion/download/MODIS/HEGtool/data'
os.environ['LD_LIBRARY_PATH']='/bess19/Image_fusion/download/MODIS/HEGtool/bin'
os.environ['PGSHOME']='/bess19/Image_fusion/download/MODIS/HEGtool/TOOLKIT_MTD'
os.environ['HEGUSER']='root'
os.environ['OMP_NUM_THREADS']='1'


path="/bess19/Image_fusion/download/MODIS/MOD07/2019"
pathoutput="/bess19/Image_fusion/download/MODIS/MOD07/Header"

if not os.path.exists(pathoutput):
    os.makedirs("Header")

# group products from the same date
datadict={}
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        print(os.path.join(path,file))
        os.system("/bess19/Image_fusion/download/MODIS/HEGtool/bin/hegtool -n {0} {1}".format(os.path.join(path,file),os.path.join(pathoutput,file.replace('.hdf','.hdr'))))
            