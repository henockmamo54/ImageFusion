# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:39:22 2021

@author: Henock
"""
import os
import sys 
import numpy as np 
import netCDF4 as nc
import pandas as pd


path='/bess19/Image_fusion/pre_process/GK2A/Cropped/VI006/'
pathoutput = '/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI006/'



if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/GK2A/CroppedConvertedTo_nc/VI006/")
 
 
for root, dirs, files in os.walk(path):
      
    for file in files:
        
        input_file = (path+file)        
        output_file=(pathoutput+file)  
        

    
    
        ncfile=nc.Dataset(input_file,'r',format='netcdf4')
         
        albedo= ncfile.variables['albedo'][:]
        latitude= ncfile.variables['latitude'][:]
        longitude= ncfile.variables['longitude'][:]
        
        #  flatten the latitude and longitude matrix
        latitude_= np.unique( np.array(latitude.data.ravel()))
        longitude_= np.unique(np.array(longitude.data.ravel()))
        val= np.array(albedo.data.ravel())
        
        # generate new albedo value matrix from flattened values
        merged_latlonalbedo = np.array([longitude_,latitude_,val]).T
        albedo_newmatrix =  np.random.uniform(0, 0, size=(longitude_.shape[0], latitude_.shape[0]))
        
        for lonindex, lonval in  enumerate(longitude_):
            _lonfiltered= merged_latlonalbedo[merged_latlonalbedo[:,0]==lonval]     
            for latindex,latval in enumerate(latitude_):
                _latfiltered= _lonfiltered[_lonfiltered[:,1]==latval]  
                if(_latfiltered.shape[0]>0):
                    albedo_newmatrix[lonindex,latindex]= _latfiltered[0,2]     
                     
        
        #=====================================================
        #=====================================================
        
        
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
        
        value[0, :, :] = albedo_newmatrix #np.random.uniform(0, 100, size=(longitude_.shape[0], latitude_.shape[0]))
        
        print('var size after adding first data', value.shape) 
        
        ds.close()

