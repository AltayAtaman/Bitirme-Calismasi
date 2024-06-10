% edge_r = [];
% 
% for i = 2:6243
%     edge_r = [edge_r;data(i,2)-data(i-1,2)];
% end
rpmdata = [];
for i = 9:6243
    num = sum(edge_r(i-8:i-1,1));
    time_dif = data(i-1,1)-data(i-8,1);
    num_per_s = num / time_dif;
    rpm = (num_per_s/20)*60;
    time = data(i-8,1);
    rpmdata = [rpmdata;time,rpm];
end