# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:04:56 2021

@author: Henock
"""

import os 

path="~/../../bess19/Image_fusion/download/GK2A/OZ/"

os.system('cd {}'.format(path)) 
os.system('find . -size 0 -delete')  
os.system('nohup python {0}downloadscript.py > {0}log_TOZ.txt &'.format(path))

