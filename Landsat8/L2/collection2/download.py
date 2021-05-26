# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:04:56 2021

@author: Henock
"""

import os 

path="~/../../bess19/Image_fusion/download/landsat8/Collection_2/L2/"

os.system('cd {}'.format(path)) 
os.system('find . -size 0 -delete')  
os.system('nohup python3 {0}downloadscript.py > {0}log_C2L2.txt &'.format(path))

