path = '/bess19/Image_fusion/'; % Path
path_h = strcat(path,'output/Harmonize/'); % 
path_s = strcat(path_h,'/Sentinel2/'); % Sentinel
path_l = strcat(path_h,'/Landsat8/'); % Landsat
path_o = strcat(path,'Gap_temp/'); % Output

path_ms = strcat(path,'output/pre_process/Sentinel2/MASK/merge'); % Fmask
path_ml = strcat(path,'output/pre_process/Landsat8/MASK/merge'); % Fmask

% Path dir
dir_s = dir(strcat(path_s,'*.tif'));
dir_l = dir(strcat(path_l,'*.tif'));

dir_ms = dir(strcat(path_ms,'*.tif'));
dir_ml = dir(strcat(path_ml,'*.tif'));

% Read files: file date and file name
[date_s, filename_s]=f_filename2date(dir_s,1);
[date_l, filename_l]=f_filename2date(dir_l,1);

[date_ms, filename_ms]=f_filename2date(dir_ms,1);
[date_ml, filename_ml]=f_filename2date(dir_ml,1);


%% Sentinel 2 
 if size(filename_s,1) ~=0

% DOY
doy_s=char(between(date_s(1),date_s(:),'Day'));
doy_s(:,end)=[];

save([path_o,'Sentinel2_NSPI_doy.mat'],'doy_s')     
     
% NBAR
temp = [path_s,filename_s(1)];
[A, geo_info]= geotiffread(temp);
info = geotiffinfo(temp);
geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
im_stack =zero(size(A,1),size(A,2),1);

for i = 1:length(filename_s)
temp = [path_h,filename_s(i)];
[temp_A, ~]= geotiffread(temp);
    
    for ii=1:size(temp_A,3)
        im_stack(:,:,end+1) = temp_A(:,:,ii);
    end



im_stack(:,:,1) = [];

geotiffwrite([path_o,'Sentinel2_NSPI.tif'],im_stack,geo_info,'GeoKeyDirectoryTag',geo_tags);

clear temp temp_A

 end
 
% Fmask
temp = [path_ms,filename_ms(1)];
[A, geo_info]= geotiffread(temp);
info = geotiffinfo(temp);
geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
im_stack =zero(size(A,1),size(A,2),1);

for i = 1:length(filename_ms)
temp = [path_h,filename_ms(i)];
[temp_A, ~]= geotiffread(temp);
    
    for ii=1:size(temp_A,3)
        im_stack(:,:,end+1) = temp_A(:,:,ii);
    end

end

im_stack(:,:,1) = [];

geotiffwrite([path_o,'Sentinel2_NSPI_mask.tif'],im_stack,geo_info,'GeoKeyDirectoryTag',geo_tags);

clear temp temp_A

end
%% Landsat 8 
 if size(filename_l,1) ~=0

% DOY
doy_l=char(between(date_l(1),date_l(:),'Day'));
doy_l(:,end)=[];

save([path_o,'Landsat8_NSPI_doy.mat'],'doy_l')

% NBAR
temp = [path_l,filename_l(1)];
[A, geo_info]= geotiffread(temp);
info = geotiffinfo(temp);
geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
im_stack =zero(size(A,1),size(A,2),1);

for i = 1:length(filename_l)
temp = [path_h,filename_l(i)];
[temp_A, ~]= geotiffread(temp);
    
    for ii=1:size(temp_A,3)
        im_stack(:,:,end+1) = temp_A(:,:,ii);
    end

end

im_stack(:,:,1) = [];

geotiffwrite([path_o,'Landsat8_NSPI.tif'],im_stack,geo_info,'GeoKeyDirectoryTag',geo_tags);

clear temp temp_A

% Fmask
temp = [path_l,filename_ml(1)];
[A, geo_info]= geotiffread(temp);
info = geotiffinfo(temp);
geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
im_stack =zero(size(A,1),size(A,2),1);

for i = 1:length(filename_ml)
temp = [path_h,filename_ml(i)];
[temp_A, ~]= geotiffread(temp);
    
    for ii=1:size(temp_A,3)
        im_stack(:,:,end+1) = temp_A(:,:,ii);
    end

end

im_stack(:,:,1) = [];

geotiffwrite([path_o,'Landsat8_NSPI_mask.tif'],im_stack,geo_info,'GeoKeyDirectoryTag',geo_tags);

clear temp temp_A

 end
