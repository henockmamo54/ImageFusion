import numpy as np
from scipy.io import loadmat, savemat
import os
import time
from functools import reduce
#start = time.time()

def ncdump(nc_fid, verb=True):
    def print_ncattr(key):
        pass
    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        for dim in nc_dims:
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        for var in nc_vars:
            if var not in nc_dims:
                print_ncattr(var)

    return nc_attrs, nc_dims, nc_vars

#calc_solar_angle(2020,1,7/6,37.3048,127.3175)
def calc_solar_angle(year,jday,hour,lat,lon):
	#References:
	#
	#  Michalsky, J., 1988: The Astronomical Almanac's algorithm for
	#     approximate solar position (1950-2050), Solar Energy 40,
	#     227-235 (but the version of this program in the Appendix
	#     contains errors and should not be used)
	#
	#  The Astronomical Almanac, U.S. Gov't Printing Office, Washington,
	#     D.C. (published every year): the formulas used from the 1995
	#     version are as follows:
	#     p. A12: approximation to sunrise/set times
	#     p. B61: solar elevation ("altitude") and azimuth
	#     p. B62: refraction correction
	#     p. C24: mean longitude, mean anomaly, ecliptic longitude,
	#             obliquity of ecliptic, right ascension, declination,
	#             Earth-Sun distance, angular diameter of Sun
	#     p. L2:  Greenwich mean sidereal time (ignoring T^2, T^3 terms)
	#
	#
	#Authors:  Dr. Joe Michalsky (joe@asrc.albany.edu)
	#          Dr. Lee Harrison (lee@asrc.albany.edu)
	#          Atmospheric Sciences Research Center
	#          State University of New York
	#          Albany, New York
	#
	#Modified by:  Dr. Warren Wiscombe (wiscombe@climate.gsfc.nasa.gov)
	#              NASA Goddard Space Flight Center
	#              Code 913
	#              Greenbelt, MD 20771
	#
	#
	#WARNING:  Do not use this routine outside the year range
	#          1950-2050.  The approximations become increasingly
	#          worse, and the calculation of Julian date becomes
	#          more involved.
	#
	#
	#
	#INPUT
	#
	#year     year (INTEGER; range 1950 to 2050)
	#
	#jday      day of year at LAT-LON location (INTEGER; range 1-366)
	#
	#hour     hour of DAY [GMT or UT] (REAL; range -13.0 to 36.0)
	#         = (local hour) + (time zone number)
	#           + (Daylight Savings Time correction; -1 or 0)
	#         where (local hour) range is 0 to 24,
	#         (time zone number) range is -12 to +12, and
	#         (Daylight Time correction) is -1 if on Daylight Time
	#         (summer half of year), 0 otherwise;
	#         Example: 8:30 am Eastern Daylight Time would be
	#
	#                     HOUR = 8.5 + 5 - 1 = 12.5
	#
	#lat      latitude [degrees]
	#         (REAL; range -90.0 to 90.0; north is positive)
	#
	#lon      longitude [degrees]
	#         (REAL; range -180.0 to 180.0; east is positive)
	#
	#
	#
	#
	#Output:
	#
	#   azi      solar azimuth angle (measured east from north,
	#            -180 to 180 degs)
	#
	#   el       solar elevation angle [-90 to 90 degs]
	#
	#   zen      solar zenith angle = 90 - EL
	#            
	#
	#Local Variables:
	#
	#  dec       Declination (radians)
	#
	#  eclong    Ecliptic longitude (radians)
	#
	#  gmst      Greenwich mean sidereal time (hours)
	#
	#  ha        Hour angle (radians, -pi to pi)
	#
	#  jd        Modified Julian date (number of days, including
	#            fractions thereof, from Julian year J2000.0);
	#            actual Julian date is JD + 2451545.0
	#
	#  lmst      Local mean sidereal time (radians)
	#
	#  mnanom    Mean anomaly (radians, normalized to 0 to 2*pi)
	#
	#  mnlong    Mean longitude of Sun, corrected for aberration
	#            (deg; normalized to 0-360)
	#
	#  oblqec    Obliquity of the ecliptic (radians)
	#
	#  ra        Right ascension  (radians)
	
	delta = year-1949
	leap = delta / 4
	jd = 32916.5 + (delta*365.0 + leap + jday) + hour / 24.0
	
	if( (year % 100)==0 and (year % 400) != 0):
		jd = jd-1
	
	time = jd - 51545.0
	
	mnlong = 280.460 + 0.9856474*time
	mnlong = mnlong % 360 
	
	if( mnlong < 0 ):
		mnlong = mnlong + 360.0
	
	mnanom = 357.528+0.9856003*time
	mnanom = mnanom % 360
	if( mnanom < 0 ):
		mnanom=mnanom+360.0
	
	mnanom=np.deg2rad(mnanom)
	
	eclong=mnlong + 1.915*np.sin(mnanom) + 0.020*np.sin(2.0*mnanom)
	eclong= eclong % 360
	if( eclong < 0 ):
		eclong= eclong+360.0
	
	oblqec = 23.439 - 0.0000004*time
	
	eclong = np.deg2rad(eclong)
	oblqec = np.deg2rad(oblqec)
	
	num=np.cos(oblqec)*np.sin(eclong)
	den = np.cos(eclong)
	ra = np.arctan(num/den)
	
	if( den < 0.0):
		ra = ra + np.pi
	elif(num < 0.0):
		ra = ra + 2 * np.pi
	
	dec = np.arcsin( np.sin(oblqec)*np.sin(eclong))
	
	gmst = 6.697375 + 0.0657098242*time+hour
	gmst = gmst % 24
	
	if(gmst < 0 ):
		gmst=gmst+24.0
	
	lmst=gmst+lon/15.0
	lmst = lmst % 24
	
	if(lmst < 0 ):
		lmst=lmst+24.0
	lmst=np.deg2rad(lmst*15.0)
	
	ha=lmst-ra
	
	if(ha < -np.pi ):
		ha = ha + np.pi*2
	
	if(ha > np.pi):
		ha = ha - np.pi*2
	
	el = np.arcsin( np.sin(dec) * np.sin( np.deg2rad(lat) ) + np.cos(dec) * np.cos(np.deg2rad(lat))* np.cos(ha) )
	
	azi = -1 * np.cos(dec) * np.sin(ha) / np.cos(el)
	
	azi = np.clip(azi,-1.0,1.0)
	azi = np.arcsin(azi)
	
	if( (np.sin(dec) - np.sin( el )*np.sin( np.deg2rad(lat) )) >= 0 ):
		if(np.sin(azi) < 0):
			azi = azi + np.pi * 2
	else:
		azi = np.pi - azi
	
	el=np.rad2deg(el)
	azi=np.rad2deg(azi)
	
	if( azi > 180.0):
		azi = azi - 360.0
	
	zen = 90.0 - el
	return (azi,el,zen)



# calc_sat_angle(38.203178, 127.253803,)

def calc_sat_angle(xlat,xlon,sat_lat,sat_lon):
	#Input:
	#
	#   xlat     pixel latitude
	#   xlon     pixel longitude
	#   sat_lat  satellite latitude
	#   sat_lon  satellite longitude
	#
	#Output:
	#
	#   azimuth      satellite azimuth angle (measured east from north,
	#            -180 to 180 degs)
	#
	#   zenith      satellite zenith angle
	
	lon = np.deg2rad(xlon - sat_lon) 
	lat = np.deg2rad(xlat - sat_lat) 
	
	beta = np.arccos(np.cos(lat) * np.cos(lon))
	
	zenith = np.arcsin( np.clip( 42164.0 * np.sin(beta) / np.sqrt(1.808e09 - 5.3725e08*np.cos(beta)),-1.0,1.0))
	zenith = np.rad2deg(zenith)
	
	azimuth = np.sin(lon) / np.sin(beta)
	azimuth = np.clip(azimuth,-1.0,1.0)
	azimuth = np.rad2deg( np.arcsin(azimuth) )
	
	if(lat<0.0):
		azimuth = 180.0 - azimuth
	
	if(azimuth<0.0):
		azimuth=azimuth+360.0
	
	azimuth=azimuth-180.0
	
	return (azimuth,zenith)

# calc_sat_angle(38.2013, 127.2507,0,128.2)
########################################################################################################################
