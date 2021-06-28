# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:42:05 2021

@author: Henock
"""


import sys 
import numpy as np 
import netCDF4 as nc
import pandas as pd


input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile4.nc'
ncfile=nc.Dataset(input_file,'r',format='netcdf4')
 
albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]

latitude_= np.unique( np.array(latitude.data.ravel()))
longitude_= np.unique(np.array(longitude.data.ravel()))
val= np.array(albedo.data.ravel())

array= np.array([longitude_,latitude_,val])




import numpy as np

# array = np.random.randint(0,10, size =(8,3))
print(array)


from scipy import interpolate

lon_list = np.arange(np.min(array[:,0]), np.max(array[:,0]), (np.max(array[:,0]) - np.min(array[:,0]) )/albedo.shape[1])
lat_list = np.arange(np.min(array[:,1]), np.max(array[:,1]), (np.max(array[:,1])- np.min(array[:,1]))/albedo.shape[0])


lon_2d, lat_2d = np.meshgrid(lon_list, lat_list)
grid_array = interpolate.griddata((array[:,-1], array[:,-2]), array[:,0],
                                  (lon_2d, lat_2d))[::-1]

