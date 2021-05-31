
import os 
import glob
import gdal
from gdalconst import GA_ReadOnly

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')

path ="/bess19/Image_fusion/download/Landsat8/L1/Extracted/"    
pathoutput="/bess19/Image_fusion/pre_process/Landsat8/Cropped/L1/"
if not os.path.exists(pathoutput):
    os.makedirs("/bess19/Image_fusion/pre_process/Landsat8/Cropped/L1/") 
    
# get extent information from MCD43A4
path_MCD43A4="/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Reprojected"
reprojectedImage_MCD43A4=(glob.glob("/bess19/Image_fusion/pre_process/MODIS/MCD43A4/Reprojected/*.tif")[0])
data = gdal.Open(reprojectedImage_MCD43A4, GA_ReadOnly)
geoTransform = data.GetGeoTransform()
minx = geoTransform[0]
maxy = geoTransform[3]
maxx = minx + geoTransform[1] * data.RasterXSize
miny = maxy + geoTransform[5] * data.RasterYSize
print ([minx, miny, maxx, maxy])
data = None
     
for root, _, files in os.walk(path):    
    for file in files: 
        if file.endswith(".TIF"): 
            print(file)
            fullpath = os.path.join(root, file)
            print(fullpath)
            # gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.217101389 38.293467877 127.372225053 38.101958373 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            # gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.212425912 38.293396512 127.42168799 38.13418831 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            gdalscript="gdal_translate   -projwin {0} {1} {2} {3} -of GTiff {4} {5}".format(miny,maxx,maxy,minx,fullpath,(pathoutput+file))
            print(gdalscript)
            os.system(gdalscript)
         
