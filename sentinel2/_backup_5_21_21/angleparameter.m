%% Sentinel2
list_xml = dir('/bess19/Image_fusion/download/sentinel2/L1/**/*TL.xml');
list_B02 = dir('/bess19/Image_fusion/download/sentinel2/L2/**/*B02_10m.jp2');
list_B03 = dir('/bess19/Image_fusion/download/sentinel2/L2/**/*B03_10m.jp2');
for i = 1:size(list_B02,1)
    a = xml2struct(strcat(list_xml(i).folder,'/',list_xml(i).name));
	b = importdata(strcat(list_B02(i).folder,'/',list_B02(i).name)); b = double(b).*0.0001;
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
    end
    RAA = abs(VAA-SAA);
    S2_SZA = imresize(SZA,size(b),'bilinear');
    S2_VZA = imresize(VZA,size(b),'bilinear');
    S2_RAA = imresize(RAA,size(b),'bilinear');
    S2_ang(:,:,1)=S2_SZA; S2_ang(:,:,2)=S2_VZA; S2_ang(:,:,3)=S2_RAA;
    % savefilename = list_B08(i).name; savefilename = "S2_" + savefilename(8:15);
    savefilename = list_B03(i).name; savefilename = "S2_" + savefilename(8:15);
    cd '/bess19/Image_fusion/download/sentinel2/S2_angle/S2_ANGLE_RESULT';
    sprintf(savefilename,'/bess19/Image_fusion/download/sentinel2/S2_angle/S2_ANGLE_RESULT')
    save(sprintf(savefilename,'/bess19/Image_fusion/download/sentinel2/S2_angle/S2_ANGLE_RESULT'),'S2_ang');
    disp(i+"_finish");
	cd '/bess19/Image_fusion/download/sentinel2/'
end