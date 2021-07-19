# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:01:38 2021

@author: Henock
"""

import netCDF4
import numpy as np

path='D:/Workplace/githubProjects/ImageFusion/GK2A/test/gk2a_ami_le1b_vi004_fd010ge_201908010100.nc'
fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/test/test.nc'

def create_file_from_source(src_file, trg_file):
    src = netCDF4.Dataset(src_file)
    trg = netCDF4.Dataset(trg_file, mode='w')

    # Create the dimensions of the file
    for name, dim in src.dimensions.items():
        trg.createDimension(name, len(dim) if not dim.isunlimited() else None)

    # Copy the global attributes
    trg.setncatts({a:src.getncattr(a) for a in src.ncattrs()})

    # Create the variables in the file
    for name, var in src.variables.items():
        trg.createVariable(name, var.dtype, var.dimensions)

        # Copy the variable attributes
        trg.variables[name].setncatts({a:var.getncattr(a) for a in var.ncattrs()})
        
        # Copy the variables values (as 'f4' eventually)
        if(name=="image_pixel_values"):
            # image_pixel_values= np.array(src.variables['image_pixel_values'][:])
            image_pixel_values = np.empty(src.variables['image_pixel_values'][:].shape) 
            image_pixel_values[:] = np.NaN
            trg.variables[name] = image_pixel_values
        else:
            trg.variables[name][:] = src.variables[name][:]
        
    # image_pixel_values= np.array(trg.variables['image_pixel_values'][:])
    # image_pixel_values = np.empty(image_pixel_values.shape) 
    # image_pixel_values[:] = np.NaN
    # trg.variables['image_pixel_values'][:] = image_pixel_values[:] 

    # Save the file
    trg.close()

create_file_from_source(path, fn)



# from scipy.io import netcdf
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
import netCDF4
 
path='D:/Workplace/githubProjects/ImageFusion/GK2A/test/test.nc'

ncfile=netCDF4.Dataset(path,'r',format='netcdf4')                
variables=list(ncfile.variables)
image_pixel_values= ncfile.variables['image_pixel_values'][:]