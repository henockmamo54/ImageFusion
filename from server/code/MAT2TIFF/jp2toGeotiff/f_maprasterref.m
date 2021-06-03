function   R = f_maprasterref(nlines,ncolumns, ybounds, xbounds)
R.XWorldLimits = xbounds;
R.YWorldLimits = ybounds;
R.RasterSize = [nlines ncolumns];
R.RasterInterpretation = 'cells';
R.ColumnsStartFrom = 'north';
R.RowsStartFrom = 'west';
