function [DOY]=f_day2doy(yr, mon, day)

leapcheck=yr./4;
if leapcheck-floor(leapcheck)>0
    modays=[0,31,59,90,120,151,181,212,243,273,304,334]';
else
    modays=[0,31,60,91,121,152,182,213,244,274,305,335]';
 end
DOY=modays(mon)+day;
