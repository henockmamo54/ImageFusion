# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:36:02 2021

@author: Henock
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 11:29:44 2021

@author: Henock
"""

import os
import sys 
import numpy as np 
import netCDF4 as nc
import pandas as pd
import random


input_file = 'D:/Workplace/githubProjects/ImageFusion/GK2A/ReprojectionCropping2/_21_cropped_gk2a_ami_le1b_vi008_fd010ge_201912290420.nc'
output_file=("test50.nc")    
ncfile=nc.Dataset(input_file,'r',format='netcdf4')
 
albedo= ncfile.variables['albedo'][:]
latitude= ncfile.variables['latitude'][:]
longitude= ncfile.variables['longitude'][:]

#  flatten the latitude and longitude matrix
latitude_= ( np.array(latitude.data.ravel()))
longitude_= (np.array(longitude.data.ravel()))
val= np.array(albedo.data.ravel())



n=random.sample(range(0, 100000000), latitude_.shape[0])
 
valpd= pd.DataFrame()
valpd["lat"]=latitude_ +n
valpd["lon"]=longitude_
valpd["val"]= val

 


# temp =valpd.set_index(['lat', 'lon'])['val'].unstack(fill_value=0)

# row_diff=latitude_.shape[0] - temp.shape[0] 
# for i in range(row_diff):
#     temp["new"+str(i)]=0
    
# if(latitude_.shape[0] !== temp.shape[0]):
#     temp["new"]=0

temp =valpd.set_index(['lat', 'lon'])['val'].unstack()

valpd.sort_values(by=["lat","lon"])

df_copy = pd.DataFrame(index=range(0,len(latitude_)),columns=range(0,len(longitude_)), dtype='float')



# ================================================== 

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d 
from matplotlib.pyplot import figure

figure(figsize=(8, 6), dpi=80)

fig = plt.figure()
ax = plt.axes(projection='3d')
 
# Data for three-dimensional scattered points
zdata = valpd.val
xdata = valpd.lat 
ydata = valpd.lon
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
# Data for three-dimensional scattered points
zdata = albedo.ravel()
xdata = latitude.ravel()
ydata = longitude.ravel()
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

# ==================================================

 

# # generate new albedo value matrix from flattened values
# merged_latlonalbedo = np.array([longitude_,latitude_,val]).T
# albedo_newmatrix =  np.random.uniform(0, 0, size=(longitude_.shape[0], latitude_.shape[0]))

# for lonindex, lonval in  enumerate(longitude_):
#     _lonfiltered= merged_latlonalbedo[merged_latlonalbedo[:,0]==lonval]     
#     for latindex,latval in enumerate(latitude_):
#         _latfiltered= _lonfiltered[_lonfiltered[:,1]==latval]  
#         if(_latfiltered.shape[0]>0):
#             albedo_newmatrix[lonindex,latindex]= _latfiltered[0,2]     
             

# #=====================================================
# #=====================================================


ds = nc.Dataset(output_file, 'w', format='NETCDF4')

time = ds.createDimension('time', None)
lat = ds.createDimension('lat', latitude_.shape[0])
lon = ds.createDimension('lon', longitude_.shape[0])

times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'

lats.units = 'degrees_north'
lats.long_name = 'latitude'
lons.units = 'degrees_east'
lons.long_name = 'longitude'

lats[:] = latitude_
lons[:] = longitude_

print('var size before adding data', value.shape) 

# value[0, :, :] = albedo_newmatrix #np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))
value[0, :, :] = temp

print('var size after adding first data', value.shape) 

ds.close()



