# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:55:29 2021

@author: Henock
"""



import sys 
import numpy as np 
import netCDF4 as nc


input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile4.nc'
ncfile=nc.Dataset(input_file,'r',format='netcdf4')
 
albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]

#=====================================================
#=====================================================
#=====================================================
#=====================================================


import netCDF4 as nc
import numpy as np

fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/test888.nc'
ds = nc.Dataset(fn, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', latitude.data.shape[0])
lon = ds.createDimension('lon', longitude.data.shape[1])

times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'

lats = latitude.data
lons = longitude.data

print('var size before adding data', value.shape)

value[0, :, :] = albedo

# print('var size after adding first data', value.shape)
# xval = np.linspace(0.5, 5.0, 10)
# yval = np.linspace(0.5, 5.0, 10)
# value[1, :, :] = np.array(xval.reshape(-1, 1) + yval)

print('var size after adding second data', value.shape)

ds.close()