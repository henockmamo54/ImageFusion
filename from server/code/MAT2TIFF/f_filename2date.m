function [date, filename] = f_filename2date(dir_p,flag)

% Juwon Kong (paradigm21c@gmaill.com)
% Seoul National University
% Environmental Ecology Lab

% flag ==1 : list of files with specific format like (.tif)
% flag ==2 : list of folders not files
% flag ==3 : list of files for GEOS yyyymmddhhmm

temp=struct2table(dir_p);
temp=table2cell(temp);
filename = temp(:,1);
filename=f_natsort(filename);

if flag ==1

tempdate= char(filename(:,1));
year = str2num(tempdate(:,end-11:end-8));
month = str2num(tempdate(:,end-7:end-6));
day = str2num(tempdate(:,end-5:end-4));
doy = f_day2doy(year,month,day);

date=datetime(year,month,day,'Format','yyyMMdd');
    
    
elseif flag ==2
filename(1:2)=[]; % delete

tempdate= char(filename(:,1));
year = str2num(tempdate(:,end-7:end-4));
month = str2num(tempdate(:,end-3:end-2));
day = str2num(tempdate(:,end-1:end));
doy = f_day2doy(year,month,day);

date=datetime(year,month,day,'Format','yyyMMdd');
    

elseif flag ==3

tempdate= char(filename(:,1));
year = str2num(tempdate(:,end-15:end-12));
month = str2num(tempdate(:,end-11:end-10));
day = str2num(tempdate(:,end-9:end-8));
hour = str2num(tempdate(:,end-7:end-6));
min = str2num(tempdate(:,end-5:end-4));
doy = f_day2doy(year,month,day);

date=datetime(year,month,day,hour,min,'Format','yyyMMddHHmm');

end

end