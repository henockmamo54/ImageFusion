NDVI1 = (L8_2018_01_01(:,:,1)-L8_2018_01_01(:,:,2))./(L8_2018_01_01(:,:,1)+L8_2018_01_01(:,:,2));
NDVI1(NDVI1>1)=nan;
imagesc(NDVI1)

red1=L8_2018_01_01(:,:,2);
red1(red1==0)=nan;
imagesc(red1);
imagesc(L8_2018_01_01(:,:,2))


%%
A = double(L8_2018_07_28(:,:,1))*0.0001;
A(A==0)=[];
A = reshape(A,[106 137]);
imagesc(B)
colormap(jet)
colorbar(); caxis([0 0.5]);
xticks([]); yticks([])
TITLE = 'Landsat8(NIR)-20180728';
title('Landsat8(NIR)-20180728.png')
savefig(gcf, TITLE);

B = [];


%% L8_ANGLE
path = '/bess19/Sungchan/KARI/L8_angle';
cd '/bess19/Sungchan/KARI/L8_angle'
L8_angle = [];
list = dir(path);
for i = 4:9:268
    L8_B4_hdr = importdata(list(i+1).name,','); 
    B4_line = str2num(L8_B4_hdr{3}(9:end)); B4_sample = str2num(L8_B4_hdr{4}(11:end));
    L8_B4_view = multibandread(list(i).name,[B4_line,B4_sample,2],'int16',0,'bsq','ieee-le');
%     L8_B5_hdr = importdata(list(i+3).name,','); 
%     B5_line = str2num(L8_B5_hdr{3}(9:end)); B5_sample = str2num(L8_B5_hdr{4}(11:end));
%     L8_B5_angle = multibandread(list(i+2).name,[B5_line,B5_sample,2],'int16',0,'bsq','ieee-le');
    L8_B4_shdr = importdata(list(i+5).name,',');
    L8_B4_solar = multibandread(list(i+4).name,[B4_line,B4_sample,2],'int16',0,'bsq','ieee-le');
    L8_shape = imread(list(i+8).name);
    RAA = abs(L8_B4_view(:,:,1)-L8_B4_solar(:,:,1)).*0.01;
    RAA = imresize(RAA, size(L8_shape));
    SZA = L8_B4_solar(:,:,2).*0.01; SZA = imresize(SZA, size(L8_shape));
    SAA = L8_B4_solar(:,:,1).*0.01; SAA = imresize(SAA, size(L8_shape));
%     SAA(SAA<=0)=NaN;
    VZA = L8_B4_view(:,:,2).*0.01; VZA = imresize(VZA, size(L8_shape)); zz= VZA(RAA<=180); VZA(RAA<=180)= -zz;
    VAA = L8_B4_view(:,:,1).*0.01; VAA = imresize(VAA, size(L8_shape));
    L8_ang = [];
    L8_ang(:,:,1) = SZA; L8_ang(:,:,2) = VZA; L8_ang(:,:,3) = RAA; 
    subplot(1,2,1); imagesc(SAA); colormap('jet'); colorbar;
    subplot(1,2,2); imagesc(VAA); colormap('jet'); colorbar;
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_AA" +list(i).name(18:25) + ".png"));
    close()
%     savefilename = list(i+1).name; savefilename = "L8_" + savefilename(18:25);
%     cd '/bess19/Sungchan/KARI/L8_angle/L8_ANGLE_RESULT'
%     save(sprintf(savefilename,'/bess19/Sungchan/KARI/L8_angle/L8_ANGLE_RESULT'),'L8_ang');
    disp(i)
    
end

a= L8_B4_solar(:,:,1).*0.01;
a(a==0)=nan;
imagesc(a);colormap('jet');

%% L8_BRDF_RESULT
path = '/bess19/Sungchan/KARI/L8_angle';
list = dir('/bess19/Sungchan/KARI/L8_angle/L8_ANGLE_RESULT/*.mat');
list_6S_nir = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*band5*.tif');
list_brdf_nir = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*nir.mat');
list_6S_red = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*band4*.tif');
list_brdf_red = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*red.mat');
list_vza = dir('/bess19/Sungchan/KARI/L8_angle/*sensor_B04.img');
list_hdr = dir('/bess19/Sungchan/KARI/L8_angle/*sensor_B04.img.hdr');
list_qa = dir('/bess19/Sungchan/KARI/L8_L2/*pixel_qa.tif');

for i = 1:30
    
    L8_QA = double(imread(list_qa(i).name));
    L8_nir_6s = double(imread(list_6S_nir(i).name)).*0.0001;
    L8_nir_6s(L8_nir_6s == -0.9999) = NaN; L8_nir_6s(L8_nir_6s<0) = NaN; L8_nir_6s(L8_nir_6s>1) = NaN;
    L8_nir_6s(L8_QA==352)=NaN; L8_nir_6s(L8_QA==368)=NaN; L8_nir_6s(L8_QA==416)=NaN;
    L8_nir_6s(L8_QA==432)=NaN; L8_nir_6s(L8_QA==480)=NaN; L8_nir_6s(L8_QA==864)=NaN;
    L8_nir_6s(L8_QA==880)=NaN; L8_nir_6s(L8_QA==928)=NaN; L8_nir_6s(L8_QA==944)=NaN;
    L8_nir_6s(L8_QA==992)=NaN; L8_nir_6s(L8_QA==328)=NaN; L8_nir_6s(L8_QA==392)=NaN;
    L8_nir_6s(L8_QA==840)=NaN; L8_nir_6s(L8_QA==904)=NaN; L8_nir_6s(L8_QA==1350)=NaN;
    L8_nir_6s(L8_QA==336)=NaN; L8_nir_6s(L8_QA==368)=NaN; L8_nir_6s(L8_QA==400)=NaN;
    L8_nir_6s(L8_QA==432)=NaN; L8_nir_6s(L8_QA==848)=NaN; L8_nir_6s(L8_QA==880)=NaN;
    L8_nir_6s(L8_QA==912)=NaN; L8_nir_6s(L8_QA==944)=NaN; L8_nir_6s(L8_QA==1352)=NaN;
    L8_nir_6s(L8_QA==324)=NaN; L8_nir_6s(L8_QA==388)=NaN; L8_nir_6s(L8_QA==836)=NaN;
    L8_nir_6s(L8_QA==900)=NaN; L8_nir_6s(L8_QA==1348)=NaN; L8_nir_6s(L8_QA==1348)=NaN; 
    
    L8_nir_BRDF = importdata(list_brdf_nir(i).name);
    L8_nir_BRDF(L8_nir_BRDF <=0) = NaN; L8_nir_BRDF(L8_nir_BRDF>=1) = NaN;
    L8_nir_BRDF(L8_QA==352)=NaN; L8_nir_BRDF(L8_QA==368)=NaN; L8_nir_BRDF(L8_QA==416)=NaN;
    L8_nir_BRDF(L8_QA==432)=NaN; L8_nir_BRDF(L8_QA==480)=NaN; L8_nir_BRDF(L8_QA==864)=NaN;
    L8_nir_BRDF(L8_QA==880)=NaN; L8_nir_BRDF(L8_QA==928)=NaN; L8_nir_BRDF(L8_QA==944)=NaN;
    L8_nir_BRDF(L8_QA==992)=NaN; L8_nir_BRDF(L8_QA==328)=NaN; L8_nir_BRDF(L8_QA==392)=NaN;
    L8_nir_BRDF(L8_QA==840)=NaN; L8_nir_BRDF(L8_QA==904)=NaN; L8_nir_BRDF(L8_QA==1350)=NaN;
    L8_nir_BRDF(L8_QA==336)=NaN; L8_nir_BRDF(L8_QA==368)=NaN; L8_nir_BRDF(L8_QA==400)=NaN;
    L8_nir_BRDF(L8_QA==432)=NaN; L8_nir_BRDF(L8_QA==848)=NaN; L8_nir_BRDF(L8_QA==880)=NaN;
    L8_nir_BRDF(L8_QA==912)=NaN; L8_nir_BRDF(L8_QA==944)=NaN; L8_nir_BRDF(L8_QA==1352)=NaN;
    L8_nir_BRDF(L8_QA==324)=NaN; L8_nir_BRDF(L8_QA==388)=NaN; L8_nir_BRDF(L8_QA==836)=NaN;
    L8_nir_BRDF(L8_QA==900)=NaN; L8_nir_BRDF(L8_QA==1348)=NaN; 
    
    L8_red_6s = double(imread(list_6S_red(i).name)).*0.0001;
    L8_red_6s(L8_red_6s == -0.9999) = NaN; L8_red_6s(L8_red_6s<0) = NaN; L8_red_6s(L8_red_6s>1) = NaN;
    L8_red_6s(L8_QA==352)=NaN; L8_red_6s(L8_QA==368)=NaN; L8_red_6s(L8_QA==416)=NaN;
    L8_red_6s(L8_QA==432)=NaN; L8_red_6s(L8_QA==480)=NaN; L8_red_6s(L8_QA==864)=NaN;
    L8_red_6s(L8_QA==880)=NaN; L8_red_6s(L8_QA==928)=NaN; L8_red_6s(L8_QA==944)=NaN;
    L8_red_6s(L8_QA==992)=NaN; L8_red_6s(L8_QA==328)=NaN; L8_red_6s(L8_QA==392)=NaN;
    L8_red_6s(L8_QA==840)=NaN; L8_red_6s(L8_QA==904)=NaN; L8_red_6s(L8_QA==1350)=NaN;
    L8_red_6s(L8_QA==336)=NaN; L8_red_6s(L8_QA==368)=NaN; L8_red_6s(L8_QA==400)=NaN;
    L8_red_6s(L8_QA==432)=NaN; L8_red_6s(L8_QA==848)=NaN; L8_red_6s(L8_QA==880)=NaN;
    L8_red_6s(L8_QA==912)=NaN; L8_red_6s(L8_QA==944)=NaN; L8_red_6s(L8_QA==1352)=NaN;
    L8_red_6s(L8_QA==324)=NaN; L8_red_6s(L8_QA==388)=NaN; L8_red_6s(L8_QA==836)=NaN;
    L8_red_6s(L8_QA==900)=NaN; L8_red_6s(L8_QA==1348)=NaN; L8_red_6s(L8_QA==1348)=NaN; 
    
    L8_red_BRDF = importdata(list_brdf_red(i).name);
    L8_red_BRDF(L8_red_BRDF <=0) = NaN; L8_red_BRDF(L8_red_BRDF>=1) = NaN;
    L8_red_BRDF(L8_QA==352)=NaN; L8_red_BRDF(L8_QA==368)=NaN; L8_red_BRDF(L8_QA==416)=NaN;
    L8_red_BRDF(L8_QA==432)=NaN; L8_red_BRDF(L8_QA==480)=NaN; L8_red_BRDF(L8_QA==864)=NaN;
    L8_red_BRDF(L8_QA==880)=NaN; L8_red_BRDF(L8_QA==928)=NaN; L8_red_BRDF(L8_QA==944)=NaN;
    L8_red_BRDF(L8_QA==992)=NaN; L8_red_BRDF(L8_QA==328)=NaN; L8_red_BRDF(L8_QA==392)=NaN;
    L8_red_BRDF(L8_QA==840)=NaN; L8_red_BRDF(L8_QA==904)=NaN; L8_red_BRDF(L8_QA==1350)=NaN;
    L8_red_BRDF(L8_QA==336)=NaN; L8_red_BRDF(L8_QA==368)=NaN; L8_red_BRDF(L8_QA==400)=NaN;
    L8_red_BRDF(L8_QA==432)=NaN; L8_red_BRDF(L8_QA==848)=NaN; L8_red_BRDF(L8_QA==880)=NaN;
    L8_red_BRDF(L8_QA==912)=NaN; L8_red_BRDF(L8_QA==944)=NaN; L8_red_BRDF(L8_QA==1352)=NaN;
    L8_red_BRDF(L8_QA==324)=NaN; L8_red_BRDF(L8_QA==388)=NaN; L8_red_BRDF(L8_QA==836)=NaN;
    L8_red_BRDF(L8_QA==900)=NaN; L8_red_BRDF(L8_QA==1348)=NaN; 
    
%     L8_6S_NDVI = (L8_nir_6s-L8_red_6s)./(L8_nir_6s+L8_red_6s);
%     L8_BRDF_NDVI = (L8_nir_BRDF-L8_red_BRDF)./(L8_nir_BRDF+L8_red_BRDF);
%     L8_6S_NIRv = L8_6S_NDVI.*L8_nir_6s;
%     L8_BRDF_NIRv = L8_BRDF_NDVI.*L8_nir_BRDF;
    
    %map2map
    subplot(1,3,1); imagesc(L8_6S_NIRv); colormap('jet'); caxis([0 0.5]); colorbar();
    title("L8\_6S\_NIRv\_" +list_6S(i).name(18:25)); xticks([]); yticks([]); 
    subplot(1,3,2); imagesc(L8_BRDF_NIRv); colormap('jet'); caxis([0 0.5]); colorbar();
    title("L8\_NBAR\_NIRv\_" +list_6S(i).name(18:25)); xticks([]); yticks([]); 
    subplot(1,3,3); imagesc(L8_BRDF_NIRv-L8_6S_NIRv); colormap('jet'); caxis([-0.1 0.1]); colorbar();
    title("L8\_NBAR-L8\_6S\_" +list_6S(i).name(18:25)); xticks([]); yticks([]); 
    
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_NIRv_map" +list_6S(i).name(18:25) + ".png"));
    close()
    
    %hist
    hist(L8_nir_BRDF(:)-L8_nir_6s(:),1000); 
    title("L8\_NBAR-L8\_6S\_" +list_6S(i).name(18:25)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_nir_hist" +list_6S(i).name(18:25)+ ".png"));
    close()
    hist(L8_red_BRDF(:)-L8_red_6s(:),1000); 
    title("L8\_NBAR-L8\_6S\_" +list_6S(i).name(18:25)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_red_hist" +list_6S(i).name(18:25)+ ".png"));
    close()
%     %scatter
%     VZA = importdata(list(i).name); VZA = VZA(:,:,2); VZA = VZA(:);
%     scatter(VZA, L8_nir_6s(:)-L8_nir_BRDF(:),1); title("L8\_NBAR-L8\_6S\_" +list_6S(i).name(18:25)); ylim([-1 1]);
%     saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_red_scatt" +list_6S(i).name(18:25)+ ".png"));
    
    disp(i)
    close()
end


list = dir('/bess19/Sungchan/KARI/L8_angle/L8_ANGLE_RESULT/*.mat');

for i = 1:1
    l8_ang = importdata(list(i).name);
    SZA = l8_ang(:,:,1); SZA(SZA==0)=NaN;
    VZA = l8_ang(:,:,2); VZA(VZA==0)=NaN;
    RAA = l8_ang(:,:,3); RAA(RAA==0)=NaN;
    subplot(1,3,1); imagesc(SZA); colormap('jet'); colorbar(); caxis([50 70]);
    title("L8\_SZA\_" + list(i).name(4:11)); xticks([]); yticks([]);
    subplot(1,3,3); imagesc(VZA); colormap('jet'); colorbar();
    title("L8\_VZA\_" + list(i).name(4:11)); xticks([]); yticks([]);
    subplot(1,3,2); imagesc(RAA); colormap('jet'); colorbar(); 
    title("L8\_RAA\_" + list(i).name(4:11)); xticks([]); yticks([]);
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/L8/',"L8_ang" +list(i).name(4:11) + ".png"));
    close()
end


%% Sentinel2
addpath(genpath('/bess19/Sungchan/KARI/S2'));
list_xml = dir('/bess19/Sungchan/KARI/S2_L1C/**/*TL.xml');
list_B02 = dir('/bess19/Sungchan/KARI/S2_L2/**/*B02_10m.jp2');
list_B03 = dir('/bess19/Sungchan/KARI/S2_L2/**/*B03_10m.jp2');

for i = 27:27
    %Surface reflectance
    xmlread(strcat(list_xml(i).folder,'/',list_xml(i).name))
    a = xml2struct(strcat(list_xml(i).folder,'/',list_xml(i).name));
    b = importdata(strcat(list_B02(i).folder,'/',list_B02(i).name)); b = double(b).*0.0001;
    c = importdata(strcat(list_B03(i).folder,'/',list_B03(i).name)); c = double(c).*0.0001;
    
    savefilename1 = list_B02(i).name; savefilename1 = "S2_B02" + savefilename1(8:15);
    savefilename2 = list_B03(i).name; savefilename2 = "S2_B03" + savefilename2(8:15);
    cd '/bess19/Sungchan/KARI/S2_angle/S2_REF';
%     save(sprintf(savefilename1,'/bess19/Sungchan/KARI/S2_angle/S2_REF'),'b');
%     save(sprintf(savefilename2,'/bess19/Sungchan/KARI/S2_angle/S2_REF'),'c');
     
    %SZA
    SZA = a.n1_colon_Level_dash_1C_Tile_ID.n1_colon_Geometric_Info.Tile_Angles.Sun_Angles_Grid;
    fun_SZA = @(x) str2double(split(squeeze(struct2cell(cell2mat(SZA(x).Zenith.Values_List.VALUES))),' '));
    fun_SAA = @(x) str2double(split(squeeze(struct2cell(cell2mat(SZA(x).Azimuth.Values_List.VALUES))),' '));
    SZA = fun_SZA(1); SAA = fun_SAA(1);
    
    VZA = a.n1_colon_Level_dash_1C_Tile_ID.n1_colon_Geometric_Info.Tile_Angles.Viewing_Incidence_Angles_Grids;
    fun_VZA = @(x) str2double(split(squeeze(struct2cell(cell2mat(VZA{x}.Zenith.Values_List.VALUES))),' '));
    fun_VAA = @(x) str2double(split(squeeze(struct2cell(cell2mat(VZA{x}.Azimuth.Values_List.VALUES))),' '));
    VZA = fun_VZA(1); VAA = fun_VAA(1);
    
    for j=2:78
        VZA = nanmean(cat(3,VZA,fun_VZA(j)),3);
        VAA = nanmean(cat(3,VAA,fun_VAA(j)),3);
    %     p=fun(i);
    %     use = find(~isnan(p));
    %     result(use) = p(use);
    end
    
%     aa = VAA(VAA>180); VAA(VAA>180)=360-aa;
%     VAA = VAA-180;
    RAA = VAA-SAA;
    zz= VZA(RAA<=0); VZA(RAA<=0)= -zz;
    
    S2_SZA = imresize(SZA,size(b),'bilinear');
    S2_VZA = imresize(VZA,size(b),'bilinear');
    S2_RAA = imresize(RAA,size(b),'bilinear');
    S2_ang(:,:,1)=SZA; S2_ang(:,:,2)=VZA; S2_ang(:,:,3)=RAA;
    subplot(1,2,1);imagesc(S2_SZA); title("S2\_SZA\_"+ list_B08(i).name(8:15)); colormap('jet'); colorbar(); xticks([]); yticks([]);
    subplot(1,2,2);imagesc(S2_VZA); title("S2\_VZA\_"+ list_B08(i).name(8:15)); colormap('jet'); colorbar(); xticks([]); yticks([]);
    set(gcf, 'Position',  [100, 100, 1600, 700])
%     saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_ang_" +list_B08(i).name(8:15) + ".png"));
    close()
    imagesc(S2_RAA); title("S2\_RAA\_"+ list_B08(i).name(8:15)); colormap('jet'); colorbar(); xticks([]); yticks([]);
%     saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_RAA_" +list_B08(i).name(8:15) + ".png"));
    close()

    savefilename = list_B08(i).name; savefilename = "S2_" + savefilename(8:15);
    cd '/bess19/Sungchan/KARI/S2_angle/S2_ANGLE_RESULT';
%     save(sprintf(savefilename,'/bess19/Sungchan/KARI/S2_angle/S2_ANGLE_RESULT'),'S2_ang');
    
    disp(i+"_finish");
end

addpath(genpath('/bess19/Sungchan/UAV/BRDF_RESULT/'));
addpath(genpath('/bess19/Sungchan/KARI/'));
list_S2_BRDF = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*S2*nir.mat');
list_S2_6S = dir('/bess19/Sungchan/KARI/S2_angle/S2_REF/*B08*.mat');
list_S2_CLD = dir('/bess19/Sungchan/KARI/S2_L2/**/*MSK_CLDPRB_20m.jp2');
list_S2_SNW = dir('/bess19/Sungchan/KARI/S2_L2/**/*MSK_SNWPRB_20m.jp2');
list_S2_ANG = dir('/bess19/Sungchan/KARI/S2_angle/S2_ANGLE_RESULT/*.mat');
list_S2_6S_ = dir('/bess19/Sungchan/KARI/S2_angle/S2_REF/*B04*.mat');
list_S2_BRDF_ = dir('/bess19/Sungchan/UAV/BRDF_RESULT/*S2*red.mat');

for i = 1:28
    
    S2_6S_NIR = importdata(list_S2_6S(i).name);
    S2_BRDF_NIR = importdata(list_S2_BRDF(i).name);
    CLD = importdata(strcat(list_S2_CLD(i).folder,'/',list_S2_CLD(i).name)); CLD = imresize(CLD, size(S2_6S_NIR));
    SNW = double(importdata(strcat(list_S2_SNW(i).folder,'/',list_S2_SNW(i).name))); SNW = imresize(SNW, size(S2_6S_NIR),'nearest');
    S2_6S_NIR(CLD>20)=NaN; S2_BRDF_NIR(CLD>20)=NaN; 
    S2_6S_NIR(SNW>1)=NaN; S2_BRDF_NIR(SNW>1)=NaN;
    S2_6S_NIR(S2_6S_NIR>1)=NaN; S2_6S_NIR(S2_6S_NIR<0)=NaN; S2_BRDF_NIR(S2_BRDF_NIR>1)=NaN; S2_BRDF_NIR(S2_BRDF_NIR<0)=NaN;
%     S2_ANG = importdata(list_S2_ANG(i).name);
    
    S2_6S_RED = importdata(list_S2_6S_(i).name);
    S2_BRDF_RED = importdata(list_S2_BRDF_(i).name);
    CLD = importdata(list_S2_CLD(i).name); CLD = imresize(CLD, size(S2_6S_NIR));
    SNW = double(importdata(list_S2_SNW(i).name)); SNW = imresize(SNW, size(S2_6S_NIR),'nearest');
    S2_6S_RED(CLD>0)=NaN; S2_BRDF_RED(CLD>0)=NaN; 
    S2_6S_RED(SNW>1)=NaN; S2_BRDF_RED(SNW>1)=NaN;
    S2_6S_RED(S2_6S_RED>1)=NaN; S2_6S_RED(S2_6S_RED<0)=NaN; S2_BRDF_RED(S2_BRDF_RED>1)=NaN; S2_BRDF_RED(S2_BRDF_RED<0)=NaN;
%     S2_ANG = importdata(list_S2_ANG(i).name);

    S2_6S_NDVI = (S2_6S_NIR-S2_6S_RED)./(S2_6S_NIR+S2_6S_RED);
    S2_6S_NIRV = S2_6S_NDVI.*S2_6S_NIR;
    S2_BRDF_NDVI = (S2_BRDF_NIR-S2_BRDF_RED)./(S2_BRDF_NIR+S2_BRDF_RED);
    S2_BRDF_NIRV = S2_BRDF_NDVI.*S2_BRDF_NIR;
    
    %map2map
    subplot(1,3,1); imagesc(S2_6S_NIR); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_6S\_NIR\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,2); imagesc(S2_BRDF_NIR); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_NBAR\_NIR\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,3); imagesc(S2_BRDF_NIR-S2_6S_NIR); colormap('jet'); caxis([-0.05 0.05]); colorbar();
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    set(gcf, 'Position',  [100, 100, 1600, 700])

    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_NIR_map" +list_S2_6S(i).name(7:14) + ".png"));
    close()
    
    subplot(1,3,1); imagesc(S2_6S_RED); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_6S\_RED\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,2); imagesc(S2_BRDF_RED); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_NBAR\_RED\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,3); imagesc(S2_BRDF_RED-S2_6S_RED); colormap('jet'); caxis([-0.1 0.1]); colorbar();
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_RED_map" +list_S2_6S(i).name(7:14) + ".png"));
    close()

    subplot(1,3,1); imagesc(S2_6S_NDVI); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_6S\_NDVI\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,2); imagesc(S2_BRDF_NDVI); colormap('jet'); caxis([0 1]); colorbar();
    title("S2\_NBAR\_NDVI\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,3); imagesc(S2_BRDF_NDVI-S2_6S_NDVI); colormap('jet'); caxis([-0.1 0.1]); colorbar();
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_NDVI_map" +list_S2_6S(i).name(7:14) + ".png"));
    close()

    subplot(1,3,1); imagesc(S2_6S_NIRV); colormap('jet'); caxis([0 0.5]); colorbar();
    title("S2\_6S\_NIRV\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,2); imagesc(S2_BRDF_NIRV); colormap('jet'); caxis([0 0.5]); colorbar();
    title("S2\_NBAR\_NIRV\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    subplot(1,3,3); imagesc(S2_BRDF_NIRV-S2_6S_NIRV); colormap('jet'); caxis([-0.1 0.1]); colorbar();
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xticks([]); yticks([]); 
    set(gcf, 'Position',  [100, 100, 1600, 700])
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_NIRV_map" +list_S2_6S(i).name(7:14) + ".png"));
    close()
   
    %hist
    hist(S2_BRDF_NIR(:)-S2_6S_NIR(:),1000); 
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_nir_hist" +list_S2_6S(i).name(7:14)+ ".png"));
    close()
    hist(S2_BRDF_RED(:)-S2_6S_RED(:),1000); 
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_RED_hist" +list_S2_6S(i).name(7:14)+ ".png"));
    close()
    hist(S2_BRDF_NDVI(:)-S2_6S_NDVI(:),1000); 
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_NDVI_hist" +list_S2_6S(i).name(7:14)+ ".png"));
    close()
    hist(S2_BRDF_NIRV(:)-S2_6S_NIRV(:),1000); 
    title("S2\_NBAR-S2\_6S\_" +list_S2_6S(i).name(7:14)); xlim([-0.1 0.1]); 
    saveas(gcf,strcat('/bess19/Sungchan/Results/KARI/S2/',"S2_NIRV_hist" +list_S2_6S(i).name(7:14)+ ".png"));
    close()
    
   
end



% VZA = a.n1_colon_Level_dash_1C_Tile_ID.n1_colon_Geometric_Info.Tile_Angles.Viewing_Incidence_Angles_Grids;
% VZA_ = cell2mat(VZA);
% 
% SZA = a.n1_colon_Level_dash_1C_Tile_ID.n1_colon_Geometric_Info.Tile_Angles.Sun_Angles_Grid.Zenith.Values_List.VALUES;
% SZA_ = cell2mat(SZA);

imagesc(S2_BRDF); colormap('jet'); 

imagesc(S2_BRDF);

