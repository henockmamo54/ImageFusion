# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:39:05 2021

@author: Henock
"""



import os 

path="~/../../bess19/Image_fusion/download/landsat8/L2/collection2/AngleParam/"

os.system('cd {}'.format(path))   
os.system('nohup python {0}angleparamGenerator.py > {0}log_angleparamGenerator.txt &'.format(path))

 