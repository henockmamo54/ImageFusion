cd '/bess19/Image_fusion/code/Fmask'

path_down ='/bess19/Image_fusion/download/';

s2_down= 'sentinel2/L1/extracted/';
l8_down= 'landsat8/L2/extracted/';

s2_mask  ='/bess19/Image_fusion/pre_process/Sentinel2/MASK/';
l8_mask  ='/bess19/Image_fusion/pre_process/Landsat8/MASK/';



for flag=1:2

    if flag ==1 % Sentinel 2

    down = s2_down;
    dir_im_down = dir(strcat(path_down,down));
    dir_im_down(1:2,:) = []; % delete

        for n=1:length(dir_im_down) 
            cd(strcat(dir_im_down(n).folder,'/',dir_im_down(n).name));
            cd(strcat(dir_im_down(n).name,'.SAFE/GRANULE/'));
            path_temp =dir;
            cd([path_temp(3).name,'/FMASK_DATA']);
            
            mask_name=dir('*_Fmask4.tif');
            
            
            temp=struct2table(mask_name);
            temp=table2cell(temp);
            filename = temp(:,1);
            filename= filename{1,1};
            
            % Location of the product
            loc_sensor = filename(:,5:10);

            % Date of the product
            year = str2num(filename(:,20:23));
            month = str2num(filename(:,24:25));
            day = str2num(filename(:,26:27));
            date=datetime(year,month,day,'Format','yyyyMMdd');
            
            [A, geo_info]=geotiffread(mask_name.name);
            mask= ones(size(A));
            ind_clear =find (A==0|1|3);
            mask(ind_clear) = 0;
            
            info = geotiffinfo(mask_name.name);
            geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
            
            geotiffwrite([s2_mask,'Sentinel2_mask_',loc_sensor,'_',char(date),'.tif'],mask,geo_info,'GeoKeyDirectoryTag',geo_tags);
        end

    elseif flag ==2 % Landsat 8

    down = l8_down;
    dir_im_down = dir(strcat(path_down,down));
    dir_im_down(1:2,:) = []; % delete
    
        for n=1:length(dir_im_down)  
            cd(strcat(dir_im_down(n).folder,'/',dir_im_down(n).name));
            
            mask_name=dir('*_Fmask4.tif');
            
            temp=struct2table(mask_name);
            temp=table2cell(temp);
            filename = temp(:,1);
            filename= filename{1,1};
            
            % Location of the product
            loc_sensor = filename(1,11:16);

            % Date of the product
            year = str2num(filename(:,18:21));
            month = str2num(filename(:,22:23));
            day = str2num(filename(:,24:25));
            date=datetime(year,month,day,'Format','yyyyMMdd');
            
            [A, geo_info]=geotiffread(mask_name.name);
            mask= ones(size(A));
            ind_clear =find (A==0|1|3);
            mask(ind_clear) = 0;
            
            info = geotiffinfo(mask_name.name);
            geo_tags = info.GeoTIFFTags.GeoKeyDirectoryTag;
            
            geotiffwrite([l8_mask,'Landsat8_mask_',loc_sensor,'_',char(date),'.tif'],mask,geo_info,'GeoKeyDirectoryTag',geo_tags);
            
        end

    end

end
cd '/bess19/Image_fusion/code/Fmask'