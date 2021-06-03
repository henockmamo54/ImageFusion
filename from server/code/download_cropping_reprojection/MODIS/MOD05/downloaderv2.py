# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:34:52 2021

@author: Henock
"""

'''
# python downloaderv2.py startdate enddate lat1 lon1 lat1 lon2
# example
# python downloaderv2.py  2019-08-01 2020-01-01 38.22346787684907 127.21710138948873 38.18195837298332 127.27222505323994
'''

import os
import sys
import modapsclient
from datetime import datetime

username = "hiik324"
password = "Ecology123"

startdate=sys.argv[1] 
enddate=sys.argv[2]   
north=sys.argv[3]     
south=sys.argv[5]     
west=sys.argv[4]      
east=sys.argv[6]

product="MOD05_L2"
collection="61"
 
startdate_obj = datetime.strptime(startdate, '%Y-%m-%d')

os.system("cd /bess19/Image_fusion/download/MODIS/MOD05") 
path = os.path.join("/bess19/Image_fusion/download/MODIS/MOD05/",str(startdate_obj.year))
if not os.path.exists(path):
     os.mkdir(path)
     

a = modapsclient.ModapsClient()


products=a.searchForFiles(products=product, startTime=startdate, 
                          endTime=enddate, north=north,south=south,
                          west=west,east=east, collection=collection)
print("Products count = > ",len(products))


for p in products:
    url=a.getFileUrls(p)[0]
    print(p,url) 
    cmd=('wget  --user hiik324 --password Ecology123 {0} --header "Authorization: Bearer C88B2F44-881A-11E9-B4DB-D7883D88392C" -P {1} '.format( url, path))
    os.system(cmd)
   