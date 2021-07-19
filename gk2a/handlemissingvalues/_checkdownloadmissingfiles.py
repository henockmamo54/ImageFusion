 
import os
import json
import netCDF4
import datetime
import numpy as np
import urllib.request as rq
 
# path="/bess19/Image_fusion/download/GK2A/L1/VI004/2019"
path="D:/Workplace/githubProjects/ImageFusion/GK2A/test"
base = datetime.datetime.strptime("08-01-2019", '%m-%d-%Y')
date_list = [(base + datetime.timedelta(days=x)).strftime("%Y%m%d") for x in range(153)]

correctvalues=['0100', '0110', '0120', '0130', '0140', '0150',
          '0200', '0210', '0220', '0230', '0240', '0250', '0300', '0310',
          '0320', '0330', '0340', '0350', '0400', '0410', '0420', '0430', 
          '0440', '0450']

lv="le1b"
ch="VI004"
AREA="FD"
key_fordownload =   "NMSC26280a3e24eb4986a669f82b906e3c7f"
resolution='010'


# group products from the same date
datadict={}
for root, dirs, files in os.walk(path):
    files.sort()      
    for file in files:
        
        filename=os.path.join(root,file)         
        filedata=(file.split('_')[-1]).replace(".nc","")
                
        _key=filedata[:8]
        
        if(_key in datadict.keys()):
            datadict[_key]["Files"].append(filedata[8:])
            datadict[_key]["count"]= datadict[_key]["count"] +1
        else:
            datadict[_key]={"count": 1, "Files":[filedata[8:]]}
         
           
    datewithnodata= set(date_list) - set(datadict.keys())
    for i in datewithnodata:
        datadict[i]={"count": 0, "Files":[]}
        

    
    keys=list(datadict.keys())
    
    for key in keys:
        print(key)
        elementcount=(datadict[key]["count"])
        try:
            if(elementcount == 24):
                del datadict[key]
            elif(elementcount != 0):
                datadict[key]["Files"]= list( set(correctvalues) - set(datadict[key]["Files"]) )
                datadict[key]["count"] = len(datadict[key]["Files"])
        except:
            print("Error , =>", key)
    
        
    with open("checkdownloadmissingfiles.json", "w") as outfile: 
        json.dump(datadict, outfile)
        
# create null valued files for mising files
src = netCDF4.Dataset(filename)
def create_file_from_source( trg_file):
    
    trg = netCDF4.Dataset(trg_file, mode='w')

    # Create the dimensions of the file
    for name, dim in src.dimensions.items():
        trg.createDimension(name, len(dim) if not dim.isunlimited() else None)

    # Copy the global attributes
    trg.setncatts({a:src.getncattr(a) for a in src.ncattrs()})

    # Create the variables in the file
    for name, var in src.variables.items():
        trg.createVariable(name, var.dtype, var.dimensions)

        # Copy the variable attributes
        trg.variables[name].setncatts({a:var.getncattr(a) for a in var.ncattrs()})
        
        # Copy the variables values (as 'f4' eventually)
        if(name=="image_pixel_values"): 
            image_pixel_values = np.empty(src.variables['image_pixel_values'][:].shape) 
            image_pixel_values[:] = np.NaN
            trg.variables[name] = image_pixel_values
        else:
            trg.variables[name][:] = src.variables[name][:]

    # Save the file
    trg.close()

# create_file_from_source(path, fn)
# gk2a_ami_le1b_vi004_fd010ge_201908150240.nc
for k in datadict.keys():
    itemscount= datadict[k]['count']
    
    if(itemscount==0):
        for t in correctvalues:            
            trg_file=path + "/gk2a_ami_" + lv + "_" + ch + "_fd"+resolution+"ge_"+ k + t +".nc"  
            create_file_from_source(trg_file) 
        for t in datadict[k]['Files']:            
            trg_file=path + "/gk2a_ami_" + lv + "_" + ch + "_fd"+resolution+"ge_"+ k + t +".nc"   
            create_file_from_source(trg_file) 
    

# generate the link for missing files and redownload
links_for_redownload=[]
for k in datadict.keys():
    itemscount= datadict[k]['count']
    
    if(itemscount==0):
        for t in correctvalues:            
            url = "http://api.nmsc.kma.go.kr:9080/api/GK2A/" + lv.upper() + '/' + ch + '/' + AREA + '/' + 'data?date=' + k + t + '&key='   
            url = url + key_fordownload
            links_for_redownload.append(url)
    else:
        for t in datadict[k]['Files']:            
            url = "http://api.nmsc.kma.go.kr:9080/api/GK2A/" + lv.upper() + '/' + ch + '/' + AREA + '/' + 'data?date=' + k + t + '&key='   
            url = url + key_fordownload
            links_for_redownload.append(url)
    

# redownload missing files
for url in links_for_redownload:
    try:
        request = rq.Request(url)
        response = rq.urlopen(request)
        rescode = response.getcode()
                    
        if not os.path.isdir(path):
            os.makedirs(path)
        if rescode == 200:
            fn = response.headers.get_filename()
            rq.urlretrieve(url, os.path.join(path, fn))
            print('Complete to download: ' + fn)
        else:                                                                                                                               
            print('Error code: ' + str(rescode)) 
    except :
        print("ERROR => ", url) 
        continue

# generate null values for missing values













