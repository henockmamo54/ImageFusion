import netCDF4 as nc
from netCDF4 import Dataset
import numpy as np
import os
import scipy
from scipy.io import loadmat, savemat
import pickle
import sys
from functools import reduce
import math
import multiprocessing as mp
sys.path.append('/usr/local/anaconda/envs/py6s-env/lib/python3.8/site-packages/Py6S')
from GK2A_anglecalculation import calc_solar_angle, calc_sat_angle, ncdump

def parfun(Fun,Args,Cores = 36,check=False,noreturn=False,sort=True):
    def forfun(proc, args):
        n = 0
        num = len(args)
        Ans = []
        ans = Ans.extend
        ansa = Ans.append
        for arg in args:
            if check:print('~ing\t','■'*int(n/num * 30)+'□'*(30-int(n/num * 30)),'%3d%%' % (int(n/num*100),),end='\r')
            n+=1
            a = Fun(*arg)
            if len(a)==0:pass
            elif len(a.shape)==1:ansa(a)
            elif len(a.shape)>1:ans(Fun(*arg))
            if check:print('~ing\t','■'*int(n/num * 30)+'□'*(30-int(n/num * 30)),'%3d%%' % (int(n/num*100),),end='\r')
        if len(Ans)>0:Q.put([proc,Ans])
    def forfun_none(args):
        n = 0
        num = len(args)
        for arg in args:
            n+=1
            if check:print('~ing\t','■'*int(n/num * 30)+'□'*(30-int(n/num * 30)),'%3d%%' % (int(n/num*100),),end='\r')
            Fun(*arg)
    interval = np.linspace(0,len(Args),Cores+1,dtype=int)
    Args = [Args[i:j] for i,j in zip(interval[:-1],interval[1:])]
    print('START')
    # No return
    if noreturn:
        P = [mp.Process(target = forfun, args=(Arg,)) for Arg in Args]
        [x.start() for x in P]
        [x.join() for x in P]
        print('FINISHED')
    else:
        Q = mp.Queue()
        P = [mp.Process(target = forfun, args=(Proc,Arg)) for Proc,Arg in enumerate(Args)]
        [x.start() for x in P]
        print(1)
        A = [Q.get() for _ in range(Cores)]
        print(2)
        [x.join() for x in P]
        if sort:A = sorted(A,key = lambda x:x[0])
        A = reduce(lambda x,y:np.vstack([x,y]),[a[1] for a in A])
        print('FINISHED')
        return A

years = np.arange(2019,2019,1)
jdays = np.arange(213,366,1)
# jdays = np.delete(jdays, [44,45,46,50,51,52,108,109])
hours = np.arange(1, 5, 1/6)
lats = loadmat('/bess19/Sungchan/1km_geos_fd_lat.mat')['geos_lat'][1360:2147,5083:5762].ravel()
lons = loadmat('/bess19/Sungchan/1km_geos_fd_lon.mat')['geos_lon'][1360:2147,5083:5762].ravel()

n=float(0)
ANGLE = []
aa = ANGLE.append
# def GK2A_ANGLE(year,jday,hour,lat,lon):
for year in years:
    for jday in jdays:
        for hour in hours:
            n+=1
            Args = [[year, jday, hour, lat, lon] for lat, lon in zip(lats, lons)]
            Fun = lambda x,y: np.array(calc_solar_angle(year,jday,hour,x,y))
            a = parfun(Fun, Args, Cores=100, check=True)
            os.chdir('/bess21/Sungchan/GK2A_RAD/INPUT/SZA_BC')
            savemat('GK2A_ANGLE_KOREA2020_%03d.mat' % (n+4958), mdict={'SZA': a})

})