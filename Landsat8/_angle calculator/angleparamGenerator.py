# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:07:18 2021

@author: Henock
"""

import glob
import os

os.chdir(r'/bess19/Image_fusion/download/landsat8/L2/collection2/extracted/')
myFiles = glob.glob('*.txt')
print(myFiles)