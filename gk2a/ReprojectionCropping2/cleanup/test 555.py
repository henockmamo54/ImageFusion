# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:02:16 2021

@author: Henock
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:20:11 2021

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

test= pd.DataFrame( np.array([longitude.data.ravel(),
                latitude.data.ravel(),
                albedo.data.ravel()
                ]).T, columns=["lon","lat","val"])



# # import numpy as np

# # lat = np.arange(0, 15, 5)
# # lon = np.arange(0, 10, 5)
# val = np.random.randint(0,10, size =len(lat)*len(lon))
# xx, yy = np.meshgrid(lon, lat)
# # array = np.array([val,  yy.ravel(), xx.ravel()]).T
# array = np.array([val,  yy.ravel(), xx.ravel()]).T
 


# no_lon = len(np.unique(lon))
# no_lat = len(np.unique(lat))

# grid_array = array[:,0].reshape((no_lat,no_lon))[::-1]
 

# lat = np.arange(0, 15, 5)
# lon = np.arange(0, 10, 5)
# val = np.random.randint(0,10, size =len(lat)*len(lon))
# xx, yy = np.meshgrid(lon, lat)
# array = np.array([val,  yy.ravel(), xx.ravel()]).T

# no_lon = len(np.unique(array[:,-1]))
# no_lat = len(np.unique(array[:,-2]))
# grid_array = array[:,0].reshape((no_lat,no_lon))[::-1]
# print(grid_array)



#=====================================================
#=====================================================


fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/test444.nc'
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

temp =  np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))

for lonindex, lonval in  enumerate(longitude_):
    for latindex,latval in enumerate(latitude_):
        tempval=test.query("lon== "+str(lonval)+" and lat == "+str(latval)).val[0]
        temp[lonindex,latindex]=tempval
        

value[0, :, :] = temp #np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))

print('var size after adding first data', value.shape)
# xval = np.linspace(0.5, 5.0, 10)
# yval = np.linspace(0.5, 5.0, 10)
# xval, yval = np.meshgrid(longitude_, latitude_)
# value[1, :, :] = np.array(xval.reshape(-1, 1) + yval)

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