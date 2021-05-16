# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:38:27 2021

@author: Henock
"""

def toDict(a):
    temp={i.split("=")[0]:i.split("=")[1] for i in a}     
    return temp

f = open("D:\Workplace\githubProjects\ImageFusion\MODIS\DELETEHEADER/MOD04_L2.A2019214.0300.061.2019214132552.hdr", "r")
# print(f.read())
temp=f.read().strip().split('\n')
v=[i for i in temp if len(i)>0]

vals= toDict(v)

'SWATH_LAT_MIN', 'SWATH_LAT_MAX', 'SWATH_LON_MIN', 'SWATH_LON_MAX',
'SWATH_X_PIXEL_RES_METERS', 'SWATH_Y_PIXEL_RES_METERS'