# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:54:06 2021

@author: Henock
"""

from pylab import *
import netCDF4

f = netCDF4.MFDataset('/usgs/data2/rsignell/models/ncep/narr/air.2m.1989.nc')