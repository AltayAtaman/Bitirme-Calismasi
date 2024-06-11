%% DC Motor Parametre Tanimlari:
L = 0.000113; % motor induktani
R = 0.199; % motor ic direnci
J = 0.0000023; % rotor atalet momenti
b = 0.000023873; % rotor surtunme katsayisi

ke = 0.0000219; % ters emk sabiti
kt = 0.0000217; % tork sabiti

z1 = (L * J / kt);
z2 = (L * b / kt);
z3 = (R * b / kt) + ke;

%% Disli Sistemi Parametre Tanimlari:
% disli oranlari
N1 = 1;
N2 = 70;
N3 = 12.77;
N4 = 8.25;

% sonumleme ve yay katsayilari
kyay = 0.17; % (n.m)/(derece)
cM = 0.022; % (n.m)/(derece*saniye)

% disli malzeme yogunluklari (al)
rhoM = 2700; 
rhoMSG = 2700;
rhoWG = 2700;
rhoDSP = 2700;
rhoDSG = 2700;
rhoSG = 2700;

% disli kutleleri
mM = 47.5 / 1000;  % kg
mMSG = 17.5 / 1000;  % kg
mWG = 100 / 1000;  % kg
mDSP = 325 / 1000;  % kg
mDSG = 89 / 1000;  % kg
mSG = 180 / 1000;  % kg

% disli yari-caplari
rM = 5.25  / 1000;  % m
rMSG = 5.25 / 1000;  % m
rWG = 5.25 / 1000;  % m
rDSP = 25 / 1000;  % m
rDSG = 49.8 / 1000;  % m
rSG = 59.4 / 1000;  % m

% eylemsizlik hesaplari
jM = 1/2*mM*((rM)^2);
%J = jM;
jMSG = 1/2*mMSG*((rMSG)^2);
jWG = 1/2*mWG*((rWG)^2);
jDSP = 1/2*mDSP*((rDSP)^2);
jDSG = 1/2*mDSG*((rDSG)^2);
jSG = 1/2*mSG*((rSG)^2);

% sonsuz disli verimi
etaWG = 0.3;

% X katsayilari hesabi
x1 = kyay/(N1*N2*N3*N4);
x2 = jSG/((N1*N2*N3*N4)^2);
x3 = jDSG/((N1*N2*N3)^2);
x4 = cM/(N1*N2);
x5 = jDSP/((N1*N2)^2);
x6 = jWG/(N1^2);
x7 = jM + jMSG;

% Y katsayilari hesabi / hesap ciktilari
y1 = x7 + x6 + (x5 + x3 + x2)/(etaWG);
y2 = x4/(etaWG);
y3 = x1/(etaWG);
