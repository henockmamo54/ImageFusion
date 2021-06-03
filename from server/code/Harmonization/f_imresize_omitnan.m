%% --------------------------------------------------------------------------
% JingWang wrote it (15-June-2019)
% %% ----------------------------------------------------------------ms ----------
function image_after=f_imresize_omitnan(image,size_vector)
[size_bef1,size_bef2]=size(image);
size_aft1=size_vector(1);
size_aft2=size_vector(2);
dx_1 = round(size_bef1/size_aft1);
dx_2 = round(size_bef2/size_aft2);
[r,c] = ndgrid(1:size_bef1, 1:size_bef2);
[~, ibin] = histc(r(:),0.5:dx_1:size_bef1+0.5);
[~, jbin] = histc(c(:),0.5:dx_2:size_bef2+0.5);
ibin(ibin==0)=size_aft1;
jbin(jbin==0)=size_aft2;
nr = max(ibin);
nc = max(jbin);
idx = sub2ind([nr nc], ibin, jbin); 
image_after = accumarray(idx, image(:), [nr*nc 1], @nanmean);
image_after = reshape(image_after, nr, nc);