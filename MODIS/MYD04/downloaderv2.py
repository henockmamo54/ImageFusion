# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:34:52 2021

@author: Henock
"""

import os
import modapsclient
from datetime import datetime

username = "hiik324"
password = "Ecology123"
startdate="2019-08-01"
enddate="2019-12-01"
north="38.22346787684907"
south="38.18195837298332"
west="127.21710138948873"
east="127.27222505323994"
product="MYD04_L2"
collection="61"
 
startdate_obj = datetime.strptime(startdate, '%Y-%m-%d')
 
path = os.path.join("./",str(startdate_obj.year))
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
   