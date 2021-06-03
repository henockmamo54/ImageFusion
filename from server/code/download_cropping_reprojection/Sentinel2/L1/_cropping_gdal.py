
'''
# python _cropping_gdal.py startdate enddate lat1 lon1 lat1 lon2
# example
# python _cropping_gdal.py  127.21710138948873 38.22346787684907 127.27222505323994 38.18195837298332
'''
 

import os
import sys
import glob

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')

lon1=sys.argv[1]     
lat1=sys.argv[2]     
lon2=sys.argv[3]      
lat2=sys.argv[4]

path ="/bess19/Image_fusion/download/Sentinel2/L1/extracted"    
pathoutput="/bess19/Image_fusion/pre_process/Sentinel2/Cropped/L1/"
if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/Sentinel2/Cropped/L1/") 
       
for root, _, files in os.walk(path):    
    for file in files: 
        if file.endswith(".jp2"): 
            print(file)
            fullpath = os.path.join(root, file)
            print(fullpath)
            # gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.217101389 38.293467877 127.372225053 38.101958373 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            # gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.212425912 38.293396512 127.42168799 38.13418831 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin {0} {1} {2} {3}  -of GTiff {4} {5}".format(lon1,lat1,lon2,lat2,(fullpath) ,(pathoutput+file))
            
            print(gdalscript)
            os.system(gdalscript)
         
