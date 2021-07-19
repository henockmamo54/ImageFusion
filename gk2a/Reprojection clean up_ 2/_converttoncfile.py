# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:38:08 2021

@author: Henock
"""

import os 
import netCDF4   
import numpy as np
import pandas as pd
from scipy.interpolate import griddata  

#================================================
#================================================
#================================================

path="Cropped/"
pathoutput="CroppedConvertedTo_nc/"
# path='/bess19/Image_fusion/pre_process/GK2A/Cropped/VI004/'
# pathoutput = '/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI004/'
# if not os.path.exists(pathoutput):
#     os.makedirs("/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI004/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        input_file = (path+file)        
        output_file=(pathoutput+file)          
        
        ncfile=netCDF4.Dataset(input_file,'r',format='netcdf4')                
        variables=list(ncfile.variables)
        
        albedo= (ncfile.variables['albedo'][:]) 
        latitude= (ncfile.variables['latitude'][:]) 
        longitude= (ncfile.variables['longitude'][:]) 
        
        albedo_=albedo.ravel()
        latitude_=latitude.ravel()
        longitude_=longitude.ravel()
        
        temp= pd.DataFrame(np.array([albedo_,latitude_,longitude_]).T,columns=["val","lat","lon"])
        mod_temp=temp.sort_values(by=["lat","lon"])
        mod_temp_val= np.array(mod_temp.val).reshape(albedo.shape)
        
        grid_x_, grid_y_ = np.mgrid[ 
                                     min(latitude_):max(latitude_)+1e-8: (max(latitude_)-min(latitude_))/latitude.shape[0],
                                    min(longitude_):max(longitude_)+1e-8: (max(longitude_)-min(longitude_))/longitude.shape[1]
                                    ]
        points_=[] 
        points_.append(mod_temp.lat)
        points_.append(mod_temp.lon)
        
        points_=np.array(points_).T
        values_=mod_temp.val
        
        
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
         
        value[0, :, :] = grid_z0_
         
        
        ds.close()
        
        






