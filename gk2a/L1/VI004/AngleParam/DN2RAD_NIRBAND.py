#!/usr/bin/env python
############################
#
# This program extract variables information and
# image_pixel_values data(Albedo) of
# GK2A Visible Ch.4 Level 1B data in netCDF4 format
#
# Input : GK2A L1B file [sample file : VI04/fd010ge] (netCDF4)
# GK2A conversion table(netCDF4)
#
# Output : sample_output.xt (ASCI)
# sample_image_pixel_data.npy (numpy format)
#
############################

import netCDF4
import numpy
import os
from scipy.io import loadmat, savemat

# inpath2 = '/bess19/Sungchan/GK-2A'
# input_ncfile_paths = [inpath2 + '/' + x for x in os.listdir(inpath2) if 'vi008' in x]
# inpath = '/bess20/Sungchan/GK2A_Data/NIR_RAD/'
# os.chdir(inpath)
# input_ncfile_paths.sort()
# output_npy_paths = [x[:-3] + '.npy' for x in os.listdir(inpath2) if 'vi008' in x]
# output_txt_paths = [x[:-3] + '.txt' for x in os.listdir(inpath2) if 'vi008' in x]
# output_npy_paths.sort()
# output_txt_paths.sort()

# input_ncfile_paths = loadmat('/bess19/Sungchan/PATH/GK2A_NIR_PATH2019.mat')['PATH']
# input_ncfile_paths = [x.strip() for x in input_ncfile_paths]
inpath2 = '/bess21/Sungchan/GK2A_NIRV/INPUT/L1B/NIR'
input_ncfile_paths = [inpath2 + '/' + x for x in os.listdir(inpath2) if 'vi008' in x]
inpath = '/bess21/Sungchan/GK2A_NIRV/RESULTS/TOA/NIR_RAD'
# inpath = '/bess20/Sungchan/GK2A_Data/KOREA/CRK_RED_RAD/'
# os.chdir(inpath)
input_ncfile_paths.sort()
output_npy_paths = [x[-43:-3] + '.npy' for x in input_ncfile_paths if 'vi008' in x]
output_txt_paths = [x[-43:-3] + '.txt' for x in input_ncfile_paths if 'vi008' in x]
# output_npy_paths = [x[:-3] + '.npy' for x in os.listdir(inpath2) if 'vi008' in x]
# output_txt_paths = [x[:-3] + '.txt' for x in os.listdir(inpath2) if 'vi008' in x]
output_npy_paths.sort()
output_txt_paths.sort()




# INPUT, OUTPUT SETTING
# sample:
#input_ncfile_paths = [
#    '/bess19/Sungchan/GK2A_Data/gk2a_ami_le1b_vi006_fd005ge_202002120200.nc',
#    '/bess19/Sungchan/GK2A_Data/gk2a_ami_le1b_vi006_fd005ge_202002120210.nc', ]

CT_path = '/bess19/Sungchan/GK2A_CT/'

# sample:
#output_npy_paths = [
#    'gk2a_ami_le1b_vi006_FD005GE_202002120200.npy',
#    'gk2a_ami_le1b_vi006_FD005GE_202002120210.npy', ]

#output_npy_paths = input_ncfile_paths




# sample:
#output_txt_paths = [
#    'gk2a_ami_le1b_vi006_FD005GE_202002120200.txt',
#    'gk2a_ami_le1b_vi006_FD005GE_202002120210.txt', ]

for input_ncfile_path, output_txt_path, output_npy_path in zip(input_ncfile_paths, output_txt_paths, output_npy_paths):
    ncfile = netCDF4.Dataset(input_ncfile_path, 'r', format='netCDF4')

    # GK2A DATA FILE READ
    ipixel = ncfile.variables['image_pixel_values']
    # ipixel_process = ipixel[1743,5420]
    ipixel_process = ipixel[1360:2147,5083:5762]

    number_of_error_pixels = ipixel.getncattr('number_of_error_pixels')
    if number_of_error_pixels > 0:
        ipixel_process[ipixel_process > 49151] = 0

    # IMAGE PIXEL VALUES BIT SIZE PER PIXEL MASKING
    channel = ipixel.getncattr('channel_name')
    if ((channel == 'VI004') or (channel == 'NR016')
            or (channel == 'VI005')):
        mask = 0b0000011111111111  # 11bit mask
    elif ((channel == 'VI006')
          or (channel == 'NR013') or (channel == 'WV063')):
        mask = 0b0000111111111111  # 12bit mask
    elif (channel == 'SW038'):
        mask = 0b0011111111111111  # 14bit mask
    else:
        mask = 0b0001111111111111  # 13bit mask

    ipixel_process_masked = numpy.bitwise_and(ipixel_process, mask)

    # CONVERT IMAGE PIXEL VALUES TO ALBEDO/BRIGHTENESS TEMPERATURE
    rad_postfix = '_con_rad.txt'
    BT_postfix = '_con_bt.txt'

    if (channel[0:2] == 'VI') or (channel[0:2] == 'NR'):
        conversion_table = numpy.loadtxt(CT_path + channel + rad_postfix, 'float64')
        convert_data = 'radiance'
    else:
        conversion_table = numpy.loadtxt(CT_path + channel + BT_postfix, 'float64')

    ipixel_process_masked_converted = conversion_table[ipixel_process_masked]

    # WRITE DATA
    #output_txt = open(output_txt_path, 'wt')
    #var_keys = ncfile.variables.keys()
    #output_txt.write("number of variable keys : %s\n" % len(var_keys))
    #for i in range(len(var_keys)):
    #    output_txt.write("%s\t%s\t%s\t%s\n"
    #                     % (i, list(var_keys)[i], ncfile.variables[list(var_keys)[i]].
    #                        dimensions, ncfile.variables[list(var_keys)[i]].dtype))
    #output_txt.close()

    print("variable list wrote to .nc")
    os.chdir('/bess21/Sungchan/GK2A_NIRV/RESULTS/TOA/NIR_RAD')
    numpy.save(output_npy_path, ipixel_process_masked_converted, False, False)
    # os.chdir(inpath)

############################
# End of Program
############################
