# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:08:49 2021

@author: Henock
"""


import sys
# from scipy.io import netcdf
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
import netCDF4 as nc

# try:
        
# # input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/gk2a_ami_le1b_vi004_fd010ge_201908110100.nc'
input_file='D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/output_ncfile4.nc'
ncfile=nc.Dataset(input_file,'r',format='netcdf4')

                
# variables=list(ncfile.variables)

# # ipixel=ncfile.variables['image_pixel_values']

# # ipixel_process = ipixel[:]

albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]


# import numpy as np
# import datetime
# from netCDF4 import Dataset,num2date,date2num
# # -----------------------
# nyears = 16;
# unout = 'days since 2000-01-01 00:00:00'
# # -----------------------
# ny, nx = latitude.shape 
# lon = longitude.ravel();
# lat = latitude.ravel();

# dataout = np.random.random((nyears,ny,nx)); # create some random data
# datesout = [datetime.datetime(2000+iyear,1,1) for iyear in range(nyears)]; # create datevalues
# # =========================
# ncout = Dataset('myfile.nc','w','NETCDF3'); # using netCDF3 for output format 
# ncout.createDimension('lon',nx);
# ncout.createDimension('lat',ny);
# ncout.createDimension('time',nyears);
# lonvar = ncout.createVariable('lon','float32',('lon'));lonvar[:] = lon;
# latvar = ncout.createVariable('lat','float32',('lat'));latvar[:] = lat;
# timevar = ncout.createVariable('time','float64',('time'));timevar.setncattr('units',unout);timevar[:]=date2num(datesout,unout);
# myvar = ncout.createVariable('myvar','float32',('time','lat','lon'));myvar.setncattr('units','mm');myvar[:] = dataout;
# ncout.close();



fn = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/heni_test5.nc'
ds = nc.Dataset(fn, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', None)
lon = ds.createDimension('lon', None)
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'


lats  = latitude 
lons  = longitude 
    
print('var size before adding data', value.shape)

value[0, :, :] = np.random.uniform(0, 100, size=(lats.data.shape[0], lons.data.shape[1]))

print('var size after adding first data', value.shape)
# xval = np.linspace(0.5, 5.0, 10)
# yval = np.linspace(0.5, 5.0, 10)
value[1, :, :] = albedo

print('var size after adding second data', value.shape)

ds.close()


# # ncfile.close()
# # ds.close()
# # except :
# #     print("Unexpected error:", sys.exc_info()[0])
# #     ncfile.close()
# #     ds.close()