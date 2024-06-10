% Fill outliers
TT = filloutliers(TT,"linear","movmedian",milliseconds(160));

% Smooth input data
TT = smoothdata(TT,"rlowess","SmoothingFactor",0.58);