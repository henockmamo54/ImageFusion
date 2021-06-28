# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:33:43 2021

@author: Henock
"""


from scipy.io import netcdf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import netCDF4

# input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/gk2a_ami_le1b_vi004_fd010ge_201908110100.nc'
# input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile.nc'
input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/21test.nc'
ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')

                
variables=list(ncfile.variables)

albedo= ncfile.variables['value'][:]
latitude= ncfile.variables['lat'][:]
longitude= ncfile.variables['lon'][:]


# import numpy as np
# from osgeo import gdal
# from osgeo import gdal_array
# from osgeo import osr
# import matplotlib.pylab as plt

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d 

fig = plt.figure()
ax = plt.axes(projection='3d')
 
albedo=albedo[0,:,:]
# Data for three-dimensional scattered points
zdata = np.sum(albedo,axis=0)
xdata = latitude.ravel()
ydata = longitude.ravel()
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');


    
    