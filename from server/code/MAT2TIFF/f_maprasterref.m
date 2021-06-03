function   R = f_maprasterref(nlines,ncolumns, ybounds, xbounds)

% % ## Juwon Kong (paradigm21c@gmaill.com)
% % ## Seoul National University
% % ## Environmental Ecology Lab

R= maprefcells();

R.XWorldLimits = xbounds;
R.YWorldLimits = ybounds;
R.RasterSize = [nlines ncolumns];
R.ColumnsStartFrom = 'north';
R.RowsStartFrom = 'west';
