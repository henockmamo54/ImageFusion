




% LAT = importdata('/bess/JCY/BESSv2/Ancillary/LAT.005d.mat');
% LON = importdata('/bess/JCY/BESSv2/Ancillary/LON.005d.mat');
 
lat1= 127.21710138948873;
lat2= 127.27222505323994;

long1= 38.18195837298332;
long2= 38.22346787684907;

s_lat =[lat1,lat1,lat2,lat2,lat1 ];
s_long= [long1,long2,long2,long1,long1];

LAT=transpose(s_lat);
LON=transpose(s_lat);
         
% years = year(datetime);
years=[2019]
% doys = 1:366; 

doys = 1:2; 
                                            
for year = years
    for doy = doys
        
        % Step 0: prepare

        % Ancillary information
        LON_ = LON;
        LON_(LON_<0) = 360 + LON_(LON_<0);
        [~,month,date,~,~,~] = datevec(datenum(year,1,doy));

        %Creat folders
        % path = sprintf('/bess19/Yulin/Data/Terra_L2/%d/%03d',year,doy);
        path = sprintf('./Terra_L2/%d/%03d',year,doy);
        if ~exist(path)
            mkdir(path)
        end
        path04 = sprintf('%s/MOD04_L2',path);
        if ~exist(path04)
            mkdir(path04)
        end
        path05 = sprintf('%s/MOD05_L2',path);
        if ~exist(path05)
            mkdir(path05)
        end
        path07 = sprintf('%s/MOD07_L2',path);
        if ~exist(path07)
            mkdir(path07)
        end
         
  
        % Step 1: select swaths 

        % Download geoMeta file    % This file provide swaths info for the next step
        if ~exist(sprintf('%s/MOD03_%d-%02d-%02d.txt',path,year,month,date))
			URL = sprintf('https://ladsweb.modaps.eosdis.nasa.gov/archive/geoMeta/6/TERRA/%d/MOD03_%d-%02d-%02d.txt',year,year,month,date);
            system(sprintf('wget  --user hiik324 --password Ecology123 %s --header "Authorization: Bearer C88B2F44-881A-11E9-B4DB-D7883D88392C" -P %s ',URL,path));
			
        end
        if ~exist(sprintf('%s/MOD03_%d-%02d-%02d.txt',path,year,month,date))
            return;
        end

        % Select daytime swaths
        [GranuleID,~,~,~,DayNightFlag,~,~,~,~,GRingLongitude1,GRingLongitude2,GRingLongitude3,GRingLongitude4,GRingLatitude1,GRingLatitude2,GRingLatitude3,GRingLatitude4] = textread(sprintf('%s/MOD03_%d-%02d-%02d.txt',path,year,month,date),'%s%s%f%f%s%f%f%f%f%f%f%f%f%f%f%f%f','delimiter',',','commentstyle','shell');
        flgDay = strcmp(DayNightFlag,'D') | strcmp(DayNightFlag,'B');
        temp = cell2mat(GranuleID(flgDay));
        hourmin = cellstr(temp(:,16:19));
        Longitude1 = GRingLongitude1(flgDay);
        Longitude2 = GRingLongitude2(flgDay);
        Longitude3 = GRingLongitude3(flgDay);
        Longitude4 = GRingLongitude4(flgDay);
        Latitude1 = GRingLatitude1(flgDay);
        Latitude2 = GRingLatitude2(flgDay);
        Latitude3 = GRingLatitude3(flgDay);
        Latitude4 = GRingLatitude4(flgDay);

        % Select land swaths
        flgPole = abs(Latitude1)>75 | abs(Latitude2)>75 | abs(Latitude3)>75 | abs(Latitude4)>75;
        flg180 = ~flgPole & (Longitude1.*Longitude3<0 | Longitude2.*Longitude4<0) & (abs(Longitude1-180)<60 | abs(Longitude2-180)<60 | abs(Longitude3-180)<60 | abs(Longitude4-180)<60);
        flgLand = false(size(hourmin));
        for i = 1:length(hourmin)
            if flgPole(i)
                flgLand(i) = true;
            else 
                lon = [Longitude1(i),Longitude2(i),Longitude3(i),Longitude4(i),Longitude1(i)];
                lat = [Latitude1(i),Latitude2(i),Latitude3(i),Latitude4(i),Latitude1(i)];
                if flg180(i)
                    lon_ = lon;
                    lon_(lon_<0) = 360 + lon_(lon_<0);
                    in = inpolygon(LON_,LAT,lon_,lat);
                else
                    in = inpolygon(LON,LAT,lon,lat);
                end
                if sum(in) > 0
                    flgLand(i) = true;
                end
            end
        end
        hm = hourmin(flgLand);
        Lon1 = Longitude1(flgLand);
        Lon2 = Longitude2(flgLand);
        Lon3 = Longitude3(flgLand);
        Lon4 = Longitude4(flgLand);
        Lat1 = Latitude1(flgLand);
        Lat2 = Latitude2(flgLand);
        Lat3 = Latitude3(flgLand);
        Lat4 = Latitude4(flgLand);
     
        % Generate swaths KML
        shp = geoshape();
        for i = 1:length(hm)
            lon = [Lon1(i),Lon2(i),Lon3(i),Lon4(i),Lon1(i)];
            lat = [Lat1(i),Lat2(i),Lat3(i),Lat4(i),Lat1(i)];
            shp = append(shp,lat,lon,'Name',hm(i));
        end
        kmlwrite(sprintf('%s/Swath.%d%03d.kml',path,year,doy),shp,'Name',shp.Name);
        save(sprintf('%s/swaths.mat',path),'hm');

        
        % Step 2: prepare download

        % List product directories
            		                             			
		 
		if ~exist(sprintf('%s/DIR_MOD04_L2.txt',path))
			
			system(sprintf('wget -O %s/DIR_MOD04_L2.txt https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_L2/%d/%03d.csv',path,year,doy));
			
		end
		if ~exist(sprintf('%s/DIR_MOD05_L2.txt',path))
			
			system(sprintf('wget -O %s/DIR_MOD05_L2.txt https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD05_L2/%d/%03d.csv',path,year,doy));
			
		end
		if ~exist(sprintf('%s/DIR_MOD07_L2.txt',path))
		   
			system(sprintf('wget -O %s/DIR_MOD07_L2.txt https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD07_L2/%d/%03d.csv',path,year,doy));
			
		end	
		
 
        % Make file look-up table 
        [name04,~,~] = textread(sprintf('%s/DIR_MOD04_L2.txt',path),'%s%s%s','headerlines',1,'delimiter',',');
        [name05,~,~] = textread(sprintf('%s/DIR_MOD05_L2.txt',path),'%s%s%s','headerlines',1,'delimiter',',');
        [name07,~,~] = textread(sprintf('%s/DIR_MOD07_L2.txt',path),'%s%s%s','headerlines',1,'delimiter',',');  %[...] = textread(...,param,value,...) customizes textread using param/value pairs
        table = {};
        hm = importdata(sprintf('%s/swaths.mat',path));
        for i = 1:length(hm)
            table{i,1} = hm(i);
             
            for j = 1:length(name04)
                name = name04{j};
                term = regexp(name,'\.','split');
                if strcmp(term{3},hm(i))
                    table{i,3} = name;
                end
            end
            for j = 1:length(name05)
                name = name05{j};
                term = regexp(name,'\.','split');
                if strcmp(term{3},hm(i))
                    table{i,4} = name;
                end
            end
            for j = 1:length(name07)
                name = name07{j};
                term = regexp(name,'\.','split');
                if strcmp(term{3},hm(i))
                    table{i,5} = name;
                end
            end
        end
        save(sprintf('%s/files.mat',path),'table');

        % Generate download list 
        fid04 = fopen(sprintf('%s/File_MOD04_L2.txt',path),'w');
        fid05 = fopen(sprintf('%s/File_MOD05_L2.txt',path),'w');
        fid07 = fopen(sprintf('%s/File_MOD07_L2.txt',path),'w');
        for i = 1:length(hm) 
            if length(table{i,3})
                fprintf(fid04,sprintf('https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_L2/%d/%03d/%s\n',year,doy,table{i,3}));
            end    
            if length(table{i,4})
                fprintf(fid05,sprintf('https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD05_L2/%d/%03d/%s\n',year,doy,table{i,4}));
            end
            if length(table{i,5})    
                fprintf(fid07,sprintf('https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD07_L2/%d/%03d/%s\n',year,doy,table{i,5}));
            end    
        end 
         
        fclose(fid04);
        fclose(fid05);
        fclose(fid07);
  
   
        %% Step 3: download data
    
        % Download using aria2c
		%system (sprintf('cd /ecology/Yulin/Data/Aqua_L2/%d/%03d/MOD04_L2' , year, doy))
        system(sprintf('wget -c -nc -P %s --user hiik324 --password Ecology123 --header "Authorization: Bearer C88B2F44-881A-11E9-B4DB-D7883D88392C" -i %s/File_MOD04_L2.txt ', path04, path)); 
		
		%system (sprintf('cd /ecology/Yulin/Data/Aqua_L2/%d/%03d/MOD05_L2' , year, doy))
        system(sprintf('wget -c -nc -P %s --user hiik324 --password Ecology123 --header "Authorization: Bearer C88B2F44-881A-11E9-B4DB-D7883D88392C" -i %s/File_MOD05_L2.txt ', path05, path));
		
		%system (sprintf('cd /ecology/Yulin/Data/Aqua_L2/%d/%03d/MOD07_L2' , year, doy))
        system(sprintf('wget -c -nc -P %s --user hiik324 --password Ecology123 --header "Authorization: Bearer C88B2F44-881A-11E9-B4DB-D7883D88392C" -i %s/File_MOD07_L2.txt ',path07, path));
		 
        disp('Done!');
    end
end	

