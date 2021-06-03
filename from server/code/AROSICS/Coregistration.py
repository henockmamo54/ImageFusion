
## Juwon Kong (paradigm21c@gmaill.com)
## Seoul National University
## Environmental Ecology Lab

import sys
import os
import glob

from arosics import COREG

path_s = "/bess19/Image_fusion/pre_process/Sentinel2/NBAR/"
path_l = "/bess19/Image_fusion/pre_process/Landsat8/NBAR/"
path_s_out ='/bess19/Image_fusion/pre_process/Sentinel2/Registration/'
path_l_out ='/bess19/Image_fusion/pre_process/Landsat8/Registration/'


## Sentinel 2

file_list = os.listdir(path_s)
##file_list = glob.glob(path_s)
file_list_tif = [file for file in file_list if file.endswith(".tif")]


for im_target in file_list_tif:
	os.chdir(path_s)
	im_reference = file_list_tif[0]
	CR = COREG(im_reference, im_target, path_out = path_s_out+im_target, fmt_out = 'GTIFF',nodata=(None, None))
	CR.correct_shifts()



## Sentinel 2 and Landsat 8

file_list = os.listdir(path_s)
file_list_tif = [file for file in file_list if file.endswith(".tif")]

im_reference = path_s+file_list_tif[0]

file_list = os.listdir(path_l)
file_list_tif = [file for file in file_list if file.endswith(".tif")]
im_target    = path_l+file_list_tif[0]

CR = COREG(im_reference, im_target, path_out = path_l_out+'A.tif', fmt_out = 'GTIFF',nodata=(None, None))
CR.correct_shifts()
print ("Co-registration between Sentinel and Landsat")

	
## Landsat 8

file_list = os.listdir(path_l)
##file_list = glob.glob(path_l)

file_list_tif = [file for file in file_list if file.endswith(".tif")]


for im_target in file_list_tif:
	os.chdir(path_l)
	im_reference = file_list_tif[0]
	CR = COREG(im_reference, im_target, path_out = path_l_out+im_target, fmt_out = 'GTIFF',nodata=(None, None))
	CR.correct_shifts()
