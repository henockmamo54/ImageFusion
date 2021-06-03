function [month, day]=f_doy2day(year,doy)
%DOY2DAY   conversion from doy time to day time

tdoy=doy;
month=0;
while tdoy > 0
   month=month+1;
   day=tdoy;
   tdoy=tdoy-sum(eomday(year,month));
end
