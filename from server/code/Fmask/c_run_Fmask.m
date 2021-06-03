path_fmask = "/bess19/Image_fusion/code/Fmask_4_3/application/run_Fmask_4_3.sh";
path_matlab = "/usr/local/MATLAB/MATLAB_Runtime/v96";

path_down ='/bess19/Image_fusion/download/';

s2_down= 'Sentinel2/L1/extracted/';
l8_down= 'Landsat8/L2/extracted/';

for flag=1:2

    if flag ==1 % Sentinel 2

    down = s2_down;
    dir_im_down = dir(strcat(path_down,down));
    dir_im_down(1:2,:) = []; % delete

        for n=1:length(dir_im_down) 
            cd(strcat(dir_im_down(n).folder,'/',dir_im_down(n).name));
            cd(strcat(dir_im_down(n).name,'.SAFE/GRANULE/'));
            path_temp =dir;
            cd(path_temp(3).name);
            status=system([path_fmask+' '+path_matlab]);
        end

    elseif flag ==2 % Landsat 8

    down = l8_down;
    dir_im_down = dir(strcat(path_down,down));
    dir_im_down(1:2,:) = []; % delete
    
        for n=1:length(dir_im_down)  
            cd(strcat(dir_im_down(n).folder,'/',dir_im_down(n).name));
            status = system([path_fmask+' '+path_matlab]);
        end

    end

end