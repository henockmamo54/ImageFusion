function [calibration_o]=f_ref_calibration_g1(unharmonized_image,reference_image)

% Harmonization using MCD43A4

[size1,size2,size3]=size(unharmonized_image);   


calibration_o=zeros(size1,size2,size3);

% Sentinel2 (Landsat 8) and MCD43A4
parfor  z=1:size3

        input_band=unharmonized_image(:,:,z);
        input_band(input_band==0)=nan;

        [mu_input,sigma_input] = normfit(input_band(input_band>eps));

        ref_band=reference_image(:,:,z);
        ref_band_downscale=f_imresize_omitnan(ref_band,[size1,size2]);
        [mu_ref,sigma_ref] = normfit(ref_band_downscale(ref_band_downscale>eps));

        param_a=sigma_ref/sigma_input;
        param_b=mu_ref-param_a*mu_input;

        calibration_temp=input_band.*param_a+param_b;
        calibration_temp(isnan(input_band))=0;
        
        if min(calibration_temp(:))<0
            reorder=sort(calibration_temp(:));
            postv_min=find(reorder>0,1,'first');
            calibration_temp(calibration_temp<0)=calibration_temp(calibration_temp<0)...
            *(reorder(postv_min)/(min(calibration_temp(:))-eps));
        end
        
        calibration_o(:,:,z)=calibration_temp;
        
end