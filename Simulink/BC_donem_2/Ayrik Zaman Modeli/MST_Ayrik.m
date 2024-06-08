clc;

N1 = 1 ; N2 = 70; N3 = 12.77;

kT = 0.17; 
cM = 0.022;

mM = 47.5 * 0.001;  % kg 
mMSG = 17.5 * 0.001;  % kg
mWG = 100 * 0.001;  % kg
mDSP = 325 * 0.001;  % kg
mSG = 180 * 0.001;  % kg

rM = 5.25 * 0.001;  % m 
rMSG = 5.25 * 0.001;  % m
rWG = 5.25 * 0.001;  % m
rDSP = 25 * 0.001;  % m
rSG = 59.4 * 0.001;  % m

rhoM = 1.220; 
rhoMSG = 1.220;
rhoWG = 1.220;
rhoDSP = 1.220;
rhoSG = 1.220;

jM = 1/2*mM*((rM)^2);
jMSG = 1/2*mMSG*((rMSG)^2);
jWG = 1/2*mWG*((rWG)^2);
jDSP = 1/2*mDSP*((rDSP)^2);
jSG = 0.5 * mSG * rSG*rSG;

eWG = 0.3;

x1 = kT/(N1*N2*N3);
x2 = jSG/((N1*N2*N3)^2);
x3 = cM/(N1*N2);
x4 = jDSP/((N1*N2)^2);
x5 = jWG/(N1^2);
x6 = jM + jMSG;

y1 = x6 + x5 + (x4 + x2)/(eWG);
y2 = x3/(eWG);
y3 = x1/(eWG);


% Ayrik Kontrolcu Girdileri:

dt = 0.1;
Ae = 0.5;
x_0 = 0; x_0_dot = 0;

fx_now = (2 .* y1 / (dt .^ 2)) - y3;
fx_pre = (y2 / (2 .* dt)) - (y1 / (dt .^ 2));
fx_fut = (y1 / (dt .^ 2)) + (y2 / (2 .* dt));

constants = [fx_now
             fx_pre
             fx_fut
             x_0
             x_0_dot
             Ae
             N1
             N2
             N3];       