# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:01:34 2021

@author: Henock
"""



 
'''
This script downloads MCD43A4.006 data given year and month
by Chongya Jiang in Sep, 2018
 
Usage: python Download.py year month day
e.g. : python Download.py 2017 7 12
''' 

import os
from sys import argv
from datetime import datetime
import urllib
import sys
import urllib.request

ROOT = 'https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.006'
root = ""
time = datetime.now()
year = 2019  
months = list(range(8,12)) #int(argv[2])
day = 1 #int(argv[3])

for month in months:
    for day in range(1,32):
        
        print(month,day)
        
        doy = int(datetime(year,month,day).timetuple().tm_yday)
        YEAR = '%d' % (year)	
        MONTH = '%02d' % (month)
        DOY = '%03d' % (doy)
        path = os.path.join(root,YEAR,DOY)
        if not os.path.exists(path): os.makedirs(path)
        PATH = '%s/%d.%02d.%02d' % (ROOT,year,month,day)
        print('Downloading MCD43D63, ' + YEAR + DOY)
        try:
            response = urllib.request.urlopen(PATH)
            for line in response.readlines():
                line= str(line)
            
                if not '.hdf">' in line: continue
                if not 'h28v05' in line: continue
            
                ind = line.find('.hdf">')
                name = line[:ind].split('"')[-1] + '.hdf'
                URL = '%s/%s' % (PATH,name)
                url = '%s/%s' % (path,name)
                print(URL)
                # os.system('wget -q -c -nc -O %s %s ' % (url,URL))
        except:
            print('ERR')
            print("Unexpected error:", sys.exc_info()[0])
            
    