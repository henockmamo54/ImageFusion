# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:27:35 2021

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

test = np.array([longitude_,latitude_,val]).T

temp =  np.random.uniform(0, 0, size=(longitude_.shape[0], latitude_.shape[0]))
for lonindex, lonval in  enumerate(longitude_):
    uu= test[test[:,0]==lonval]
    print(uu,lonval)
    for latindex,latval in enumerate(latitude_):
        vv= uu[uu[:,1]==latval]  
        if(vv.shape[0]>0):
            temp[lonindex,latindex]= vv[0,2]      
            print(vv,latval)

#=====================================================
#=====================================================


fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/test777.nc'
ds = nc.Dataset(fn, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', latitude_.shape[0])
lon = ds.createDimension('lon', longitude_.shape[0])

times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'

lats[:] = latitude_
lons[:] = longitude_

print('var size before adding data', value.shape)

# temp =  np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))
      

value[0, :, :] = temp #np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))

print('var size after adding first data', value.shape)
 
print('var size after adding second data', value.shape)

ds.close()













#=====================================================
#=====================================================


# import netCDF4 as nc
# import numpy as np

# fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/test888.nc'
# ds = nc.Dataset(fn, 'w', format='NETCDF4')

# time = ds.createDimension('time', None)
# lat = ds.createDimension('lat', latitude.data.ravel().shape[0])
# lon = ds.createDimension('lon', latitude.data.ravel().shape[0])

# times = ds.createVariable('time', 'f4', ('time',))
# lats = ds.createVariable('lat', 'f4', ('lat',))
# lons = ds.createVariable('lon', 'f4', ('lon',))
# value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
# value.units = 'Unknown'

# lats = no_lon
# lons = no_lat

# print('var size before adding data', value.shape)

# value[0, :, :] = grid_array

# # print('var size after adding first data', value.shape)
# # xval = np.linspace(0.5, 5.0, 10)
# # yval = np.linspace(0.5, 5.0, 10)
# # value[1, :, :] = np.array(xval.reshape(-1, 1) + yval)

# print('var size after adding second data', value.shape)

# ds.close()