function info = f_getMetadata(file)

tline = '';
fid = fopen(file,'r');
while ischar(tline)
    
    tline = fgetl(fid);
    if ~ischar(tline)
        break;
    end
    %<HORIZONTAL_CS_CODE>EPSG:32630</HORIZONTAL_CS_CODE>
    if strfind(tline,'<HORIZONTAL_CS_CODE>')
        id = strfind(tline,'EPSG:');
        if isempty(id)
            error('EPSG not found');
        else
            tline = tline(id(1)+5:end);
            id = strfind(tline,'<');
            info.code = str2num(tline(1:id-1));
        end
    end
    
    if strfind(tline,'<Size resolution="10">')
        %get row
        tline = fgetl(fid);
        info.res_10.nrow = getVal(tline);
        
        %get col
        tline = fgetl(fid);
        info.res_10.ncol = getVal(tline);
    end
    
    if strfind(tline,'<Size resolution="20">')
        %get row
        tline = fgetl(fid);
        info.res_20.nrow = getVal(tline);
        
        %get col
        tline = fgetl(fid);
        info.res_20.ncol = getVal(tline);
    end
    
    if strfind(tline,'<Size resolution="60">')
        %get row
        tline = fgetl(fid);
        info.res_60.nrow = getVal(tline);
        
        %get col
        tline = fgetl(fid);
        info.res_60.ncol = getVal(tline);
    end
    
    if strfind(tline,'  <Geoposition resolution="10">')
        %get ulx
        tline = fgetl(fid);
        info.res_10.ulx = getVal(tline);
        
        %get uly
        tline = fgetl(fid);
        info.res_10.uly = getVal(tline);
    end
    
    if strfind(tline,'  <Geoposition resolution="20">')
        %get ulx
        tline = fgetl(fid);
        info.res_20.ulx = getVal(tline);
        
        %get uly
        tline = fgetl(fid);
        info.res_20.uly = getVal(tline);
    end
    if strfind(tline,'  <Geoposition resolution="60">')
        %get ulx
        tline = fgetl(fid);
        info.res_60.ulx = getVal(tline);
        
        %get uly
        tline = fgetl(fid);
        info.res_60.uly = getVal(tline);
    end
    
    
end

fclose(fid);
end


function val = getVal(tline)
id    = strfind(tline,'>');
tline = tline(id(1)+1:end);
id    = strfind(tline,'<');
val   = str2num(tline(1:id-1));
end