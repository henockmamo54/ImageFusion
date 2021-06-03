function [calibration_o]=f_ref_calibration_g2(unharmonized_image,temp_image,reference_image,wg_date)

% Extract parameter for MODIS-GK2A calibration output : Juwon Kong
% 2021-03-23

% If the similarity between MCD43A4 and GK2A were 'A'
% We assume that only the half of A remains after 16days.
% exp(0.6931)=0.5.

coef = (0.6931./16);
wg = exp((-1)*coef*wg_date);


[~,~,size3]=size(reference_image);   
[size1,size2,~]=size(temp_image);

calibration_o=zeros(size1,size2,size3);


reference = reference_image;

% parameter1 = zeros(size3,1);
% parameter2 = zeros(size3,1);

% MCD43A4 and GK2A
for  z=1:size3

        input_band=temp_image(:,:,z);
        input_band(input_band==0)=nan;
        [mu_input,sigma_input] = normfit(input_band(input_band>eps));
        ref_band=reference(:,:,z);
        reference_downscale=f_imresize_omitnan(ref_band,[size1,size2]);
        [mu_ref,sigma_ref] = normfit(reference_downscale(reference_downscale>eps));
        

        param_a=sigma_input/sigma_ref;
        param_b=(mu_ref-mu_input)*wg;
        
%         if param_b <0
%             param_b=param_b*(-1);
%         end

        input_band = unharmonized_image(:,:,z);
        calibration_temp=input_band.*param_a+param_b;
        calibration_temp(isnan(input_band))=0;
        
        if min(calibration_temp(:))<0
            reorder=sort(calibration_temp(:));
            postv_min=find(reorder>0,1,'first');
            calibration_temp(calibration_temp<0)=calibration_temp(calibration_temp<0)...
            *(reorder(postv_min)/(min(calibration_temp(:))-eps));
        end
        
        calibration_o(:,:,z)=calibration_temp;
        
%         parameter1(z) = param_a ;
%         parameter2(z)= param_b;
      
end