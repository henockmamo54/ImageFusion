 
import os
import json
import datetime

 
path="/bess19/Image_fusion/download/GK2A/L1/VI008/2019"

base = datetime.datetime.strptime("08-01-2019", '%m-%d-%Y')
date_list = [(base + datetime.timedelta(days=x)).strftime("%Y%m%d") for x in range(153)]

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
        
    correctvalues=['0100', '0110', '0120', '0130', '0140', '0150',
              '0200', '0210', '0220', '0230', '0240', '0250', '0300', '0310',
              '0320', '0330', '0340', '0350', '0400', '0410', '0420', '0430', 
              '0440', '0450']
    
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