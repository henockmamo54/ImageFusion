function [calibration_o]=f_ref_calibration_land(unharmonized_image,reference_image)
    % setting
     k = 10; % number of kmean image segmentation class

    % Harmonization using MCD43A4
    [size1,size2,size3]=size(unharmonized_image);   
    [size_r1,size_r2,~]=size(reference_image);

    calibration_o=zeros(size1,size2,size3);
    calibration_temp =nan(size1,size2);
    calibration_k=zeros(size1,size2);

    % Unsupervised clustering (K-mean segmentation)

    temp = unharmonized_image;
    temp(temp < 0 | temp> 1) = nan;
   
    temp(:,:,5) = (temp(:,:,4)-temp(:,:,3))./ (temp(:,:,4)+temp(:,:,3)); % NDVI
    temp(:,:,5) = temp(:,:,5) .* 10000;
    temp(:,:,6) = (temp(:,:,2)-temp(:,:,4))./ (temp(:,:,2)+temp(:,:,4)); % NWVI
    temp(:,:,6) = temp(:,:,6) .* 10000;
    temp = int16(temp);
   
    num_classes = k;
    mean_Class=[];
    mask=nan(size(temp,1),size(temp,2),6);

    
 parfor bn=1:6 % 5 는 NDVI 넣었을때!
  [mean_Class(:,bn),mask(:,:,bn)]=Class_Kmeans(temp(:,:,bn),num_classes);   %Using K-Means classification method
 end

  Max_image_kmeans=max(mask,[],3);
  mask_kmeans=Max_image_kmeans; 

  mask_downscale=f_imresize_omitnan(mask_kmeans,[size_r1,size_r2]);


    
% Planet and reference
for  z=1:size3
    
    for land = 1:num_classes
    
        [row, col]=find(mask_kmeans == land);
        [row_down, col_down]=find(mask_downscale ~= land);
    


        input_band=unharmonized_image(:,:,z);  
        input_band(input_band==0)=nan;
        
        input_band_downscale = f_imresize_omitnan(input_band,[size_r1,size_r2]);
        input_band_downscale(row_down, col_down)=nan;
        [mu_input,sigma_input] = normfit(input_band_downscale(input_band_downscale>eps));

        ref_band=reference_image(:,:,z);
        ref_band(row_down, col_down)=nan;
        [mu_ref,sigma_ref] = normfit(ref_band(ref_band>eps));

        param_a=sigma_ref/sigma_input;
        param_b=mu_ref-param_a*mu_input;

        calibration_temp(row,col)=input_band(row,col).*param_a+param_b;
        calibration_temp(isnan(input_band))=0;
        
        if min(calibration_temp(:))<0
            reorder=sort(calibration_temp(:));
            postv_min=find(reorder>0,1,'first');
            calibration_temp(calibration_temp<0)=calibration_temp(calibration_temp<0)...
            *(reorder(postv_min)/(min(calibration_temp(:))-eps));
        end
        
        calibration_k(row,col)=calibration_temp(row,col);
        
        
    end

        calibration_o(:,:,z)=calibration_k;
end