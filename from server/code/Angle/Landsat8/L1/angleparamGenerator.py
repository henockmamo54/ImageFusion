# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:07:18 2021

@author: Henock
"""
 
import os

path ="/bess19/Image_fusion/download/Landsat8/L1/Extracted"
filelist = []

for root, dirs, files in os.walk(path):
    
    for file in files:
        filename=os.path.join(root,file)
        print(filename)
        
        #append the file name to the list
        if filename.endswith("ANG.txt"):
            filelist.append(os.path.join(root,file))
    
	
    
#print all the file names
for name in filelist:
    print(name) 
    os.system(r"/bess19/Image_fusion/code/Angle/Landsat8/l8_angles/l8_angles {0} BOTH 1 -b 2,3,4,5".format(name))
    