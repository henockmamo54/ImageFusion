

% Written by Juwon Kong

cd /bess19/Image_fusion/code/MAT2TIFF

path_nbar = '/bess19/Image_fusion/pre_process/';
path_down ='/bess19/Image_fusion/download/';

s2_down= 'Sentinel2/L2/extracted/';
l8_down= 'Landsat8/L2/extracted/';

s2_nbar = 'Sentinel2/NBAR/'; %  GLOBAL paramter
l8_nbar = 'Landsat8/NBAR/';

% change it based on ROI
% s2_loc = 'T52SCH';  % s2_tile; % 'T52SCH';
% l8_loc = '116033';% l8_tile; % '116033';



for ss=1:2

if ss == 1    
    nbar = s2_nbar;
    down = s2_down;
%     loc_target = s2_loc;
    
elseif ss == 2
    nbar = l8_nbar;
    down = l8_down;
%     loc_target = l8_loc;
end


dir_im_nbar = dir(strcat(path_nbar,nbar,'*.mat'));
if ~isempty(dir_im_nbar)
[im_date, im_name] = f_filename2date(dir_im_nbar,1); 


for i = 1: length(im_name)
temp = im_name{i};
temp_loc_target{i,1} = temp(end-15:end-13);
end

clear temp

date_t = unique(im_date);

loc_t = unique(temp_loc_target);

loc_t = char(loc_t);
loc_target = char(temp_loc_target);

dir_im_down = dir(strcat(path_down,down));

for n =1:length(date_t)
    
idx_d = im_date == date_t(n);

 for ii=1:length(loc_target)
    idx_l(ii,1) = strcmp(loc_target(ii,:),loc_t(n,:));
 end
 
 idx = find(idx_d .* idx_l ==1);
 
    for i = 1:length(idx)
         temp = importdata(strcat(path_nbar,nbar,im_name{idx(i)}));
         temp(isnan(temp)) = 3.0;
         sen_nbar(:,:,i)=temp.*100000;
    end
    
    sen_nbar=int16(sen_nbar);
   
    [geo_info, geo_tags] = f_dir2geoinfo(dir_im_down,date_t(n),loc_target(idx_l,:),ss);
    
    cd /bess19/Image_fusion/code/MAT2TIFF
    
    if ss==1 % Sentinel 2 using external function 
        geotiffwrite([path_nbar,nbar,'Sentienl2_NBAR_',char(date_t(n)),'.tif'],sen_nbar,geo_info,'GeoKeyDirectoryTag',geo_tags);
        
    elseif ss==2 % Landsat 8 internal function
        geotiffwrite([path_nbar,nbar,'Landsat8_NBAR_',char(date_t(n)),'.tif'],sen_nbar,geo_info,'GeoKeyDirectoryTag',geo_tags);
        
    end


end

clear sen_nbar temp

end
end
