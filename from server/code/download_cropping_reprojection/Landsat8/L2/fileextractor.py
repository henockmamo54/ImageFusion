# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:59:34 2021

@author: Henock
"""

import os
import zipfile
import tarfile

directory="/bess19/Image_fusion/download/Landsat8/L2"
for filename in os.listdir(directory):
    try:
        if filename.endswith("tar.gz"):  
            path_to_zip_file=os.path.join(directory, filename)
            directory_to_extract_to= os.path.join(directory,"Extracted",filename)
            print(path_to_zip_file,'\n',directory_to_extract_to)
            with tarfile.open(path_to_zip_file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to.replace(".tar.gz",""))
    except:
        print("Error")
    