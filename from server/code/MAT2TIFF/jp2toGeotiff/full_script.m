
jp2_file='T52SCH_20200919T021609_B02_10m.jp2';
xmlGranuleFile = 'MTD_TL.xml';

img = imread(jp2_file);
info = f_getMetadata(xmlGranuleFile);
[x,y] = size(img);
%since we have three spatial resolution (10m, 20m and 60m) we need to make the distinction based
%on the size of the S2 image being processed
%create the R georeferencing matrix
if x == info.res_10.nrow  &&   y == info.res_10.ncol
    option.ModelPixelScaleTag = [10;10;0];
    option.ModelTiepointTag = [0;0;0;info.res_10.ulx;info.res_10.uly;0];
    bbox =  [  info.res_10.ulx,  info.res_10.uly - 10*info.res_10.nrow ; info.res_10.ulx + 10*info.res_10.ncol,  info.res_10.uly  ];
    R = f_maprasterref(info.res_10.nrow,info.res_10.ncol, [info.res_10.uly - 10*info.res_10.nrow info.res_10.uly ], [info.res_10.ulx  info.res_10.ulx + 10*info.res_10.ncol ]);
end
if x == info.res_20.nrow  &&   y == info.res_20.ncol
    option.ModelPixelScaleTag = [20;20;0];
    option.ModelTiepointTag = [0;0;0;info.res_20.ulx;info.res_20.uly;0];
    R = f_maprasterref(info.res_20.nrow,info.res_20.ncol, [info.res_20.uly - 20*info.res_20.nrow info.res_20.uly ], [info.res_20.ulx  info.res_20.ulx + 20*info.res_20.ncol ]);
    bbox =  [  info.res_20.ulx,  info.res_20.uly - 20*info.res_20.nrow ; info.res_20.ulx + 20*info.res_20.ncol,  info.res_20.uly  ];
end
if x == info.res_60.nrow  &&   y == info.res_60.ncol
    option.ModelPixelScaleTag = [60;60;0];
    option.ModelTiepointTag = [0;0;0;info.res_60.ulx;info.res_60.uly;0];
    bbox =  [  info.res_60.ulx,  info.res_60.uly - 60*info.res_60.nrow ; info.res_60.ulx + 60*info.res_60.ncol,  info.res_60.uly  ];
    R = f_maprasterref(info.res_60.nrow,info.res_60.ncol, [info.res_60.uly - 60*info.res_60.nrow info.res_60.uly ], [info.res_60.ulx  info.res_60.ulx + 60*info.res_60.ncol ]);
end
option.GTModelTypeGeoKey = 1;
option.ProjectedCSTypeGeoKey = info.code;
% filenameOut = fullfile(outputfolder,[name,'.tif']);
filenameOut = fullfile('A.tif');
f_geotiffwrite(filenameOut, bbox, img, 32, option); 
