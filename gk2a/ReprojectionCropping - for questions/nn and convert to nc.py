# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:59:33 2021

@author: Henock
"""
  
import numpy as np  
import netCDF4 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.interpolate import griddata 

input_file='output_ncfile.nc'
output_file = 'converted_ncfile.nc' 

ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')                
variables=list(ncfile.variables)

albedo= (ncfile.variables['albedo'][:]) 
latitude= (ncfile.variables['latitude'][:]) 
longitude= (ncfile.variables['longitude'][:]) 

albedo_=albedo.ravel()
latitude_=latitude.ravel()
longitude_=longitude.ravel()

grid_x_, grid_y_ = np.mgrid[ 
                            min(latitude_):max(latitude_): ((max(latitude_)-min(latitude_))/latitude.shape[0]),
                            min(longitude_):max(longitude_): ((max(longitude_)-min(longitude_))/longitude.shape[1])
                            ]


points_=[]
points_.append(latitude_)
points_.append(longitude_)
points_=np.array(points_).T
values_=albedo_


grid_z0_ = griddata(points_, values_, (grid_x_, grid_y_), method='nearest')


# #=====================================================
# #=====================================================


ds = netCDF4.Dataset(output_file, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', grid_x_.shape[0])
lon = ds.createDimension('lon', grid_y_.shape[1])

times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'

lats.units = 'degrees_north'
lats.long_name = 'latitude'
lons.units = 'degrees_east'
lons.long_name = 'longitude'

lats[:] = np.unique(grid_x_)
lons[:] = np.unique(grid_y_)

print('var size before adding data', value.shape) 

# value[0, :, :] = albedo_newmatrix #np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))
value[0, :, :] = grid_z0_

print('var size after adding first data', value.shape) 

ds.close()
