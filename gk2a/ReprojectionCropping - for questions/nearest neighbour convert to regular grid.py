# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:37:31 2021

@author: Henock
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
from scipy.interpolate import griddata

# def func(x, y):
#     return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

# grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

# rng = np.random.default_rng()
# points = rng.random((1000, 2))
# values = func(points[:,0], points[:,1])

# grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')

# import matplotlib.pyplot as plt
# plt.subplot(221)
# plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
# plt.plot(points[:,0], points[:,1], 'k.', ms=1)
# plt.title('Original')

# plt.subplot(222)
# plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
# plt.title('Nearest')

#================================================

#================================================

#================================================


import netCDF4 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

input_file='output_ncfile.nc'
ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')                
variables=list(ncfile.variables)

albedo= (ncfile.variables['albedo'][:]) 
latitude= (ncfile.variables['latitude'][:]) 
longitude= (ncfile.variables['longitude'][:]) 

albedo_=albedo.ravel()
latitude_=latitude.ravel()
longitude_=longitude.ravel()

grid_x_, grid_y_ = np.mgrid[ 
                            min(latitude_):max(latitude_): (max(latitude_)-min(latitude_))/latitude.shape[0],
                            min(longitude_):max(longitude_): (max(longitude_)-min(longitude_))/longitude.shape[1]
                            ]
points_=[]
points_.append(latitude_)
points_.append(longitude_)
points_=np.array(points_).T
values_=albedo_


grid_z0_ = griddata(points_, values_, (grid_x_, grid_y_), method='nearest')



import matplotlib.pyplot as plt
plt.subplot(221)
plt.imshow(albedo.T,  origin='lower')
# plt.imshow(albedo.T, origin='lower')
# plt.plot(points_[:,0], points_[:,1], 'k.', ms=1)
plt.title('Original')

plt.subplot(222)
plt.imshow(grid_z0_.T,  origin='lower')
plt.title('Nearest')






























