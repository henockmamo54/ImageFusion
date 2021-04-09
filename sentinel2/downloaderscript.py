# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:13:01 2021

@author: Henock
"""

import os

startdate="2019-09-26T06:00:00.000Z"
enddate="2019-12-01T06:00:00.000Z"

lat1="38.18195837298332"
long1= "127.21710138948873"
lat2="38.22346787684907"
long2= "127.27222505323994"

missionname="Sentinel-2"
producttype_level1="S2MSI1C"
producttype_level2="S2MSI2A"
downloadoption="product"
listcount= 100
level1destination="/bess19/Image_fusion/download/sentinel2/L1"
level2destination="/bess19/Image_fusion/download/sentinel2/L2"


level1Datadownloadscript= '''bash dhusget_0.sh -m {0} -s {1} -e {2} -c {3},{4}:{5},{6} -T {7} -l {8} -C '{10}/products-list.csv' -o '{9}' -O '{10}'  -w 1 -W 1'''.format(missionname,startdate,enddate,long1,lat1,long2,lat2, producttype_level1,listcount,downloadoption,level1destination)
level2Datadownloadscript= '''bash dhusget_0.sh -m {0} -s {1} -e {2} -c {3},{4}:{5},{6} -T {7} -l {8} -C '{10}/products-list.csv' -o '{9}' -O '{10}'  -w 1 -W 1'''.format(missionname,startdate,enddate,long1,lat1,long2,lat2, producttype_level2,listcount,downloadoption,level2destination)

os.system(level1Datadownloadscript)
os.system(level2Datadownloadscript)
