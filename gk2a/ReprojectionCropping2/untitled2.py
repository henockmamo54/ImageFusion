# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:33:56 2021

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
 

fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/heni_test5.nc'
ds = nc.Dataset(fn, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', None)
lon = ds.createDimension('lon', None)
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'


lats  = latitude[:,0].data 
lons  = longitude[0,:].data 
    
print('var size before adding data', value.shape)

# value[0, :, :] = np.random.uniform(0, 100, size=(lats.shape[0], lons.shape[0]))

print('var size after adding first data', value.shape)
# xval = np.linspace(0.5, 5.0, 10)
# yval = np.linspace(0.5, 5.0, 10)
value[0, :, :] = albedo

print('var size after adding second data', value.shape)

ds.close()


# # ncfile.close()
# # ds.close()
# # except :
# #     print("Unexpected error:", sys.exc_info()[0])
# #     ncfile.close()
# #     ds.close()