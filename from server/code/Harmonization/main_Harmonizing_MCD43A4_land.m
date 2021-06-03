%% Path setting

% Path
path = '/bess19/Image_fusion/'; % Path
path_s = strcat(path,'pre_process/Sentinel2/Registration/'); % Sentinel
path_l = strcat(path,'pre_process/Landsat8/Registration/'); % Landsat
path_m = strcat(path,'pre_process/MODIS/Cropped'); % MODIS
path_g =strcat(path,'pre_process/GK2A/Cropped'); % GK2A
path_o = strcat(path,'output/Harmonize/'); % Output

% Path dir
dir_s = dir(strcat(path_s,'*.tif'));
dir_l = dir(strcat(path_l,'*.tif'));
dir_m = dir(strcat(path_m,'*.tif'));
dir_g = dir(strcat(path_g,'*.tif'));

% Read files: file date and file name
[date_s, filename_s]=f_filename2date(dir_s,1);
[date_l, filename_l]=f_filename2date(dir_l,1);
[date_m, filename_m]=f_filename2date(dir_m,1);
[date_g, filename_g]=f_filename2date(dir_g,1);

% For output file
out_date_s = datestr(date_s,'yyyyMMdd');
out_date_l = datestr(date_l,'yyyyMMdd');
out_date_g = datestr(date_g,'yyyyMMdd');


%% Harmonizing Sentinel 2 NBAR to MCD43A4

nfile = length(filename_s);

if nfile ~= 0
for i =1:nfile
    % Read Sentinel
    [sentinel_image,~]=geotiffread(strcat(path_s,filename_s{i}));
    sentinel_image = double(sentinel_image);
    sentinel_image = sentinel_image./10000;
    
    % Info for saving
    info = geotiffinfo(strcat(path_s,filename_s{i}));
    geoTags = info.GeoTIFFTags.GeoKeyDirectoryTag;
    
    % Read MCD43A4
    idx_m= find(date_m==date_s(i));
    [modis_image,~]=geotiffread(strcat(path_m,filename_m{idx_m}));
    modis_image = double(modis_image);
    reference_image = modis_image./10000;
    
    % Calibration
    calibration_o = f_ref_calibration_land(sentinel_image,reference_image);
    calibration_o=calibration_o*10000;
    calibration_o = int32(calibration_o);

    % Save harmonized Sentinel2 to geotiff file
    geotiffwrite([path_o,'Sentienl2/sentinel2_cal_',out_date_s(i,:),'.tif'],calibration_o,geo_info,'GeoKeyDirectoryTag',geoTags);
    
end
end
%% Harmonizing Landsat 8 NBAR to MCD43A4
nfile = length(filename_l);

if nfile ~= 0
    for i =1:nfile
    % Read Landsat
    [landsat_image,~]=geotiffread(strcat(path_l,filename_l{i}));
    landsat_image = double(landsat_image);
    landsat_image = landsat_image./10000;
    
    % Info for saving
    info = geotiffinfo(strcat(path_l,filename_l{i}));
    geoTags = info.GeoTIFFTags.GeoKeyDirectoryTag;
    
    % Read MCD43A4
    idx_m= find(date_m==date_l(i));
    [modis_image,~]=geotiffread(strcat(path_m,filename_m{idx_m}));
    modis_image = double(modis_image);
    reference_image = modis_image./10000;
    
    % Calibration
    calibration_o = f_ref_calibration_land(landsat_image,reference_image);
    calibration_o=calibration_o*10000;
    calibration_o = int32(calibration_o);

    % Save harmonized Landsat 8 to geotiff file
    geotiffwrite([path_o,'Landsat8/Lansdat8_cal_',out_date_l(i,:),'.tif'],calibration_o,geo_info,'GeoKeyDirectoryTag',geoTags);
    
    end
end
%% Harmonizing GK2A NBAR to MCD43A4

nfile = length(filename_g);

if nfile ~= 0
for i =1:nfile

    % Read GK2A
    [gk2a_image,~]=geotiffread(strcat(path_g,filename_g{i}));
    gk2a_image = double(gk2a_image);
    gk2a_image = gk2a_image./10000;
    
    % Info for saving
    info = geotiffinfo(strcat(path_g,filename_g{i}));
    geoTags = info.GeoTIFFTags.GeoKeyDirectoryTag;
  
    % Read MCD43A4
    idx= find(date_g(i)==date_m);
     
    if (isempty(idx) == 1) 
    temp_diff=caldays(between(date_g(i),date_m,'Days'));
    temp_diff=abs(temp_diff);    
    [diff_m,ind_m] = min(temp_diff);
    
    [modis_image,~]=geotiffread(strcat(path_m,filename_m{idx_m}));
    modis_image = double(modis_image);
    reference_image = modis_image./10000;
    
    gt=find(date_m(ind_m) == date_g);
    
    [gk2a_temp,~]=geotiffread(strcat(path_g,filename_g{gt}));
    gk2a_temp = double(gk2a_temp);
    gk2a_temp = gk2a_temp./10000;
    
    [calibration_o]=f_ref_calibration_g2(gk2a_image,gk2a_temp,modis_image,diff_m);

    elseif (isempty(idx) ~= 1)
    idx_m= find(date_m==date_g(i));
    [modis_image,~]=geotiffread(strcat(path_m,filename_m{idx_m}));
    modis_image = double(modis_image);
    reference_image = modis_image./10000;
    
    % Calibration
    [calibration_o] = f_ref_calibration_g1(gk2a_image,reference_image);
    calibration_o=calibration_o*10000;
    calibration_o = int32(calibration_o);
    end
    
    % Save harmonized GK2A to geotiff file
    geotiffwrite([path_o,'GK2A/GK2A_cal_',out_date_g(i,:),'.tif'],calibration_o,geo_info,'GeoKeyDirectoryTag',geoTags);
    
end

end
