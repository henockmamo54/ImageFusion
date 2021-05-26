import glob, os 

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/landsat8/L2/collection1/extracted/"    
pathoutput="/bess19/Image_fusion/download/landsat8/L2/collection1/Cropped/"
 
if not os.path.exists(pathoutput):
    os.makedirs("Cropped") 
    
for root, _, files in os.walk(path):
    for file in files: 
        if file.endswith(".tif"): 
            print(file)
            fullpath = os.path.join(root, file)
            print(fullpath)
            # gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.217101389 38.293467877 127.372225053 38.101958373 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.212425912 38.293396512 127.42168799 38.13418831 -of GTiff "+ (fullpath) + " "+(pathoutput+file)
            print(gdalscript)
            os.system(gdalscript)
         
