# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:39:19 2021

@author: Henock
"""
'''
# python downloadscript.py startdate enddate lat1 lon1 lat1 lon2
# example
# python downloadscript.py  2019-08-01 2020-01-01  
'''
 
import os
import sys
import modapsclient
from datetime import datetime
from datetime import timedelta 

def down_gk2a(_st, lv, ch, AREA, down_dir):                                                                             
    # To download gk2a data from NMSC
    # made by sb.lee 2021-01-25
    import urllib.request as rq
    import datetime as dt
    import os
    ################################
    st = dt.datetime.strptime(str(_st), "%Y%m%d%H%M")
    st = st + timedelta(hours=1)
        
    while (st.hour<5):                                                               
        key =   "NMSC26280a3e24eb4986a669f82b906e3c7f"                                                                                                                     
        url = "http://api.nmsc.kma.go.kr:9080/api/GK2A/" + lv + '/' + ch + '/' + AREA + '/' + 'data?date=' + st.strftime("%Y%m%d%H%M") + '&key='   
        # $input_url="http://api.nmsc.kma.go.kr:8080/api/GK2A/LE1B/VI004/EA/data?date=202007021604&req_div=oper01"
        url = url + key
        
        try:
            request = rq.Request(url)
            response = rq.urlopen(request)
            rescode = response.getcode()
            
            if not os.path.isdir(down_dir):
                os.makedirs(down_dir)
            if rescode == 200:
                fn = response.headers.get_filename()
                rq.urlretrieve(url, os.path.join(down_dir, fn))
                print('Complete to download: ' + fn)
            else:                                                                                                                               
                print('Error code: ' + str(rescode)) 
        except :
            print("ERROR => ", url)
            st = st + timedelta(minutes=10)
            continue
        
        st = st + timedelta(minutes=10)




startdate=sys.argv[1]
enddate=sys.argv[2]

startdate = datetime.strptime(startdate, '%Y-%m-%d')
enddate = datetime.strptime(enddate, '%Y-%m-%d')

path = os.path.join("/bess19/Image_fusion/download/GK2A/L1/VI006",str(startdate.year))
lv="LE1B"
ch="VI006"
AREA="FD"
date= startdate
while date <= enddate:
    try:
        print(date)       
        temp=str(date).replace(':','').replace('-','').replace(' ','')[:-2]
        down_gk2a(temp,lv,ch,AREA,path)
    except:
        print("Error on ", str(date))
    
    date= date + timedelta(days=1)
