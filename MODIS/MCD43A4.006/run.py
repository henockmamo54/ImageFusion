# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:26:19 2021

@author: Henock
"""



import os 

path="/bess19/Image_fusion/download/MODIS/MCD43A4/"

os.system('cd {}'.format(path)) 
os.system('find . -size 0 -delete')  
os.system('nohup python {0}batch_downloader.py > {0}log_MCD43A4.txt &'.format(path))