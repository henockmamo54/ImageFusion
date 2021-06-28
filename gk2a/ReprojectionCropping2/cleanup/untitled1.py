# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:41:35 2021

@author: Henock
"""

from scipy.io import netcdf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import netCDF4

input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile.nc'
ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')

                
variables=list(ncfile.variables)
albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]

# ==================================================================
# ==================================================================
# ==================================================================
# ==================================================================
# ==================================================================

# import numpy as np
# import datetime
# from netCDF4 import Dataset,num2date,date2num
# # -----------------------
# nyears = 16;
# unout = 'days since 2000-01-01 00:00:00'
# # -----------------------
# ny, nx = (latitude.shape[0],longitude.shape[0])#(250, 186)
# lon = np.linspace(9,30,nx);
# lat = np.linspace(50,60,ny);

# dataout = np.random.random((nyears,ny,nx)); # create some random data
# # datesout = [datetime.datetime(2000+iyear,1,1) for iyear in range(nyears)]; # create datevalues
 
# dataout[1, :, :] = albedo
# # =========================
# ncout = Dataset('myfile.nc','w','NETCDF3'); # using netCDF3 for output format 
# ncout.createDimension('lon',nx);
# ncout.createDimension('lat',ny);
# ncout.createDimension('time',nyears);
# lonvar = ncout.createVariable('lon','float32',('lon'));lonvar[:] = lon;
# latvar = ncout.createVariable('lat','float32',('lat'));latvar[:] = lat;
# # timevar = ncout.createVariable('time','float64',('time'));timevar.setncattr('units',unout);timevar[:]=date2num(datesout,unout);
# myvar = ncout.createVariable('myvar','float32',('time','lat','lon'));myvar.setncattr('units','mm');myvar[:] = dataout;
# ncout.close();