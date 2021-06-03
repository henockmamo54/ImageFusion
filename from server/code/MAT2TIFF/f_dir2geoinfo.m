function [geo_info, geo_tags] = f_dir2geoinfo(dir_im_down,date_t,loc_target,flag)

% Editted by Juwon Kong

cd /bess19/Image_fusion/code/MAT2TIFF

temp=struct2table(dir_im_down);
temp=table2cell(temp);
filename = temp(:,1);
filename=f_natsort(filename);

filename(1:2)=[]; % delete (Need to add path_t +2)
temp= char(filename(:,1));


if flag ==1 % Sentinel 2
    

    % Location of the product
    loc_sensor = temp(:,39:44);

    % Date of the product
    year = str2num(temp(:,12:15));
    month = str2num(temp(:,16:17));
    day = str2num(temp(:,18:19));
    date=datetime(year,month,day,'Format','yyyyMMdd');


elseif flag ==2 % Landsat 8
  
    % Location of the product
    loc_sensor = temp(:,11:16);

    % Date of the product
    year = str2num(temp(:,18:21));
    month = str2num(temp(:,22:23));
    day = str2num(temp(:,24:25));
    date=datetime(year,month,day,'Format','yyyyMMdd');

end


% Filtering date
ind_date=find(date == date_t);

% Filtering target location
for i= 1:length(loc_sensor)
ind_loc(i)=strcmp(loc_sensor(i,:), loc_target);
end



for i=1:length(ind_date)
    
  ind_temp=find(find (ind_loc'==1) == ind_date(i));
     if size(ind_temp)~= 0
         path_t = ind_temp;    
     end
     
end


path_t=path_t + 2; % add deleted number

cd(dir_im_down(path_t).folder);

dir_im_t=dir(strcat('./',dir_im_down(path_t).name));

cd(strcat('./',dir_im_down(path_t).name));

if flag ==1
    cd(strcat(dir_im_down(path_t).name,'.SAFE/GRANULE/'));
    path_temp =dir;
    cd(path_temp(3).name);
    dir_temp = dir;
    xmlGranuleFile = 'MTD_TL.xml';
    
    cd /bess19/Image_fusion/code/MAT2TIFF
    
    info = f_getMetadata(strcat(dir_temp(5).folder,'/',xmlGranuleFile));
    
    
    % The spatial resolution fo Sentinel 2 Band 2 3 4 8 = 10m
    
     % create the R georeferencing matrix
% if x == info.res_10.nrow  &&   y == info.res_10.ncol
    R_10m = f_maprasterref(info.res_10.nrow,info.res_10.ncol, [info.res_10.uly - 10*info.res_10.nrow info.res_10.uly ], [info.res_10.ulx  info.res_10.ulx + 10*info.res_10.ncol ]);
% end
% if x == info.res_20.nrow  &&   y == info.res_20.ncol
%     R_20m = f_maprasterref(info.res_20.nrow,info.res_20.ncol, [info.res_20.uly - 20*info.res_20.nrow info.res_20.uly ], [info.res_20.ulx  info.res_20.ulx + 20*info.res_20.ncol ]);
% end
% if x == info.res_60.nrow  &&   y == info.res_60.ncol
%     R_60m = f_maprasterref(info.res_60.nrow,info.res_60.ncol, [info.res_60.uly - 60*info.res_60.nrow info.res_60.uly ], [info.res_60.ulx  info.res_60.ulx + 60*info.res_60.ncol ]);
% end

    geo_info = R_10m;
    
 % Extract GeoTags from Metafile
    geo_tags = f_getGeoTags_sentinel2(strcat(dir_temp(5).folder,'/',xmlGranuleFile));
 
elseif flag ==2
    
    % Read Spatial referencing object from Band1
    
%     ver=['Release R' version('-release')];
%     if str2num(ver(10:13)) < 2020
    [~, geo_info]= geotiffread(dir_im_t(4).name);
%     elseif str2num(ver(10:13)) >= 2020
%     [~,geo_info] readgeoraster(dir_im_t(4).name);
%     end
    info = geotiffinfo(dir_im_t(4).name);
    geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;

end    