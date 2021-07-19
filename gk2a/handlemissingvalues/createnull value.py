# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:00:25 2021

@author: Henock
"""



# from scipy.io import netcdf
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
import netCDF4
import copy

import xarray as xr


 
path='D:/Workplace/githubProjects/ImageFusion/GK2A/test/gk2a_ami_le1b_vi004_fd010ge_201908010100.nc'

ncfile=netCDF4.Dataset(path,'r',format='netcdf4')                
variables=list(ncfile.variables)
image_pixel_values= np.array(ncfile.variables['image_pixel_values'][:])
image_pixel_values = np.empty(image_pixel_values.shape) 
image_pixel_values[:] = np.NaN



fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/test/test.nc'
ds = netCDF4.Dataset(fn, 'w', format='NETCDF4')
ds = (ncfile)

ds.close() 



input = xr.open_dataset('path.nc')
input.to_netcdf('copy_of_ncfile.nc')



# # from scipy.io import netcdf
# import numpy as np
# # import matplotlib
# # import matplotlib.pyplot as plt
# import netCDF4
 
# path='D:/Workplace/githubProjects/ImageFusion/GK2A/test/test.nc'

# ncfile=netCDF4.Dataset(path,'r',format='netcdf4')                
# variables=list(ncfile.variables)
# # image_pixel_values= np.array(ncfile.variables['image_pixel_values'][:])