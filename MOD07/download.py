# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:04:56 2021

@author: Henock
"""



import os 

import os 

path="~/../../bess19/Image_fusion/download/MODIS/MOD05/"

os.system('cd {}'.format(path)) 
os.system('find . -size 0 -delete')  
os.system('nohup python {0}downloaderv2.py > {0}log_MOD05.txt &'.format(path))

