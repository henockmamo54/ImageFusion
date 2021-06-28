# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:30:48 2021

@author: Henock
"""
 

from scipy.io import netcdf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import netCDF4

# input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/gk2a_ami_le1b_vi004_fd010ge_201908110100.nc'
input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile.nc'
ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')

                
variables=list(ncfile.variables)

# ipixel=ncfile.variables['image_pixel_values']

# ipixel_process = ipixel[:]

albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]


# ==================================================


import numpy as np
from osgeo import gdal
from osgeo import gdal_array
from osgeo import osr
import matplotlib.pylab as plt