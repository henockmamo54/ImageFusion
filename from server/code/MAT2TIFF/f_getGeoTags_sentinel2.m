function geoTags = f_getGeoTags_sentinel2(file)

% from  'MTD_TL.xml' read information

% http://geotiff.maptools.org/spec/geotiff6.html#6.3.1.4

tline = '';
fid = fopen(file,'r');
while ischar(tline)
    
    tline = fgetl(fid);
    if ~ischar(tline)
        break;
    end

%% GTModelTypeGeoKey
%     
%     Ranges:
%    0              = undefined
%    [   1,  32766] = GeoTIFF Reserved Codes
%    32767          = user-defined
%    [32768, 65535] = Private User Implementations
% GeoTIFF defined CS Model Type Codes:
%    ModelTypeProjected   = 1   /* Projection Coordinate System         */
%    ModelTypeGeographic  = 2   /* Geographic latitude-longitude System */
%    ModelTypeGeocentric  = 3   /* Geocentric (X,Y,Z) Coordinate System */
%  
% Notes:
%    1. ModelTypeGeographic and ModelTypeProjected
%       correspond to the FGDC metadata Geographic and
%       Planar-Projected coordinate system types.
    geoTags.GTModelTypeGeoKey= 1;
    %% GTRasterTypeGeoKey
%    Ranges:
%    0             = undefined
%    [   1,  1023] = Raster Type Codes (GeoTIFF Defined)
%    [1024, 32766] = Reserved
%    32767         = user-defined
%    [32768, 65535]= Private User Implementations
% Values:
%    RasterPixelIsArea  = 1
%    RasterPixelIsPoint = 2
% Note: Use of "user-defined" or "undefined" raster codes is not recommended.
    
 geoTags.GTRasterTypeGeoKey= 1;
    
%% GTCitationGeoKey / GeogCitationGeoKey
     if strfind(tline,'<HORIZONTAL_CS_NAME>')
        id = strfind(tline,'WGS84');
        if isempty(id)
            error('CS_NAME not found');
        else
            tline = tline(id(1):end);
            id = strfind(tline,'<');
            geoTags.GTCitationGeoKey = tline(1:id-1);
            geoTags.GeogCitationGeoKey = tline(1:6);
        end
    end    % WGS84 / UTM zone 52N
%     

%% ProjectedCSTypeGeoKey
%     
    if strfind(tline,'<HORIZONTAL_CS_CODE>')
        id = strfind(tline,'EPSG:');
        if isempty(id)
            error('EPSG not found');
        else
            tline = tline(id(1)+5:end);
            id = strfind(tline,'<');
            geoTags.ProjectedCSTypeGeoKey = str2num(tline(1:id-1));
        end
    end
    
    
%%     ProjLinearUnitsGeoKey
%   There are several different kinds of units that may be used in geographically related raster data:
%   linear units, angular units, units of time (e.g. for radar-return), CCD-voltages, etc. 
%   For this reason there will be a single, unique range for each kind of unit, broken down into the following currently defined ranges:

%    Ranges:
%    0             = undefined
%    [   1,  2000] = Obsolete GeoTIFF codes
%    [2001,  8999] = Reserved by GeoTIFF
%    [9000,  9099] = EPSG Linear Units.
%    [9100,  9199] = EPSG Angular Units.
%    32767         = user-defined unit
%    [32768, 65535]= Private User Implementations
% Linear Unit Values (See the ESPG/POSC tables for definition):
%    Linear_Meter =	9001
%    Linear_Foot =	9002
%    Linear_Foot_US_Survey =	9003
%    Linear_Foot_Modified_American =	9004
%    Linear_Foot_Clarke =	9005
%    Linear_Foot_Indian =	9006
%    Linear_Link =	9007
%    Linear_Link_Benoit =	9008
%    Linear_Link_Sears =	9009
%    Linear_Chain_Benoit =	9010
%    Linear_Chain_Sears =	9011
%    Linear_Yard_Sears =	9012
%    Linear_Yard_Indian =	9013
%    Linear_Fathom =	9014
%    Linear_Mile_International_Nautical =	9015

      geoTags.ProjLinearUnitsGeoKey = 9001;
    
%% GeogAngularUnitsGeoKey

% Angular Units Codes
% These codes shall be used for any key that requires specification of an angular unit of measurement.
% Angular Units    
%    Angular_Radian =	9101
%    Angular_Degree =	9102
%    Angular_Arc_Minute =	9103
%    Angular_Arc_Second =	9104
%    Angular_Grad =	9105
%    Angular_Gon =	9106
%    Angular_DMS =	9107
%    Angular_DMS_Hemisphere =	9108
   
geoTags.GeogAngularUnitsGeoKey =9102;
   
    
end

fclose(fid);
end


function val = getVal(tline)
id    = strfind(tline,'>');
tline = tline(id(1)+1:end);
id    = strfind(tline,'<');
val   = str2num(tline(1:id-1));
end