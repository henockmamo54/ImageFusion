


import glob, os 

os.system('export PATH="/usr/local/gdal/2.4.2/bin:$PATH"')
os.system('export PATH="/usr/local/anaconda/bin:$PATH"')
 


path ="/bess19/Image_fusion/download/landsat8/L2/collection2/extracted/"    
pathoutput="/bess19/Image_fusion/download/landsat8/L2/collection2/Cropped/"
os.chdir(path) 

if not os.path.exists(pathoutput):
    os.makedirs("Cropped") 
    
for root, _, files in os.walk(path):
    for file in files: 
        if file.endswith(".TIF"): 
            print(file)
            gdalscript="gdal_translate   -projwin_srs 'EPSG:4326'  -projwin 127.217101389 38.293467877 127.372225053 38.101958373 -of GTiff "+ (path+file) + " "+(pathoutput+file)
            print(gdalscript)
            os.system(gdalscript)
        