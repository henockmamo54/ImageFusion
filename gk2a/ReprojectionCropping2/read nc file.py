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
# input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile.nc'
input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/_21_cropped_gk2a_ami_le1b_vi008_fd010ge_201912290420.nc'
ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')

                
variables=list(ncfile.variables)

# ipixel=ncfile.variables['image_pixel_values']

# ipixel_process = ipixel[:]

albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]


# ==================================================


# import numpy as np
# from osgeo import gdal
# from osgeo import gdal_array
# from osgeo import osr
# import matplotlib.pylab as plt

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d 
from matplotlib.pyplot import figure

figure(figsize=(8, 6), dpi=80)

fig = plt.figure()
ax = plt.axes(projection='3d')


# ax = plt.axes(projection='3d')
# # Data for a three-dimensional line
# zline = albedo.ravel()
# xline = latitude.ravel()
# yline = longitude.ravel()
# ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = albedo.ravel()
xdata = latitude.ravel()
ydata = longitude.ravel()
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
