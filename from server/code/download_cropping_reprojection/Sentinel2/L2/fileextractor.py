# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:59:34 2021

@author: Henock
"""

import os
import zipfile


directory="/bess19/Image_fusion/download/Sentinel2/L2"
for filename in os.listdir(directory):
    try:
        if filename.endswith(".zip"):  
            path_to_zip_file=os.path.join(directory, filename)
            directory_to_extract_to= os.path.join(directory,"extracted",filename)
            print(path_to_zip_file,'\n',directory_to_extract_to)
            with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to.replace(".zip",""))
    except:
        print("Error")
    