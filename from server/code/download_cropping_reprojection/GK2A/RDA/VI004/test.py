import netCDF4
import numpy
import os
from scipy.io import loadmat, savemat


# inpath2 = '/bess21/Sungchan/GK2A_NIRV/INPUT/L1B/NIR'
inpath2 = '/bess19/Image_fusion/download/GK2A/L1/VI008/2019'


input_ncfile_paths = [inpath2 + '/' + x for x in os.listdir(inpath2) ]
 
output_npy_paths = [x[-43:-3] + '.npy' for x in input_ncfile_paths ]
output_txt_paths = [x[-43:-3] + '.txt' for x in input_ncfile_paths ]
 

CT_path = '/bess19/Sungchan/GK2A_CT/'
 
for i in range (len(input_ncfile_paths)):
    print(i, "=>",input_ncfile_paths[i])
    ncfile = netCDF4.Dataset([inpath2 + '/' + x for x in os.listdir(inpath2) ][i],'r',format='netcdf4')

    ncfile = netCDF4.Dataset(input_ncfile_paths[i],'r',format='netcdf4')