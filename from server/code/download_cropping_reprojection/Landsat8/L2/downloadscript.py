

'''
# python downloadscript.py startdate enddate lat1 lon1 lat1 lon2
# example
# python3 downloadscript.py  2019-08-01 2020-01-01 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907
# python3 downloadscript.py  2020-08-01 2020-10-01 127.21710138948873 38.18195837298332 127.27222505323994 38.22346787684907
'''
import os
import sys
import json
from landsatxplore.api import API
from landsatxplore.earthexplorer import EarthExplorer

startdate=sys.argv[1] 
enddate=sys.argv[2]   
lon1=sys.argv[3]     
lat1=sys.argv[4]     
lon2=sys.argv[5]      
lat2=sys.argv[6]

outputpath="/bess19/Image_fusion/download/Landsat8/L2"

username="henockmao54@snu.ac.kr"
password="jh|WMe3A9DAK44n"

api = API("henockmao54@snu.ac.kr","jh|WMe3A9DAK44n")

scenes = api.search(
    dataset='landsat_ot_c2_l2',
    # bbox= (127.21710138948873,38.18195837298332,127.27222505323994,38.22346787684907),    
    bbox= (lon1,lat1,lon2,lat2),    
    start_date=startdate,
    end_date=enddate  
)

print(str(len(scenes))," scenes found.")
 

ee = EarthExplorer(username, password)

for s in scenes:
    print(s)
    print(s["display_id"])
    ee.download(s["entity_id"], output_dir=outputpath)
 