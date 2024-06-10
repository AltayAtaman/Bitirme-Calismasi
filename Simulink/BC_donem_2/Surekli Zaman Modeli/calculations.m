%% Transfer Fonksiyonu Eldesi

tf_dc_num = [kt * J, kt * b];
tf_dc_denom = [L * J, (L * b) + (R * J), (R * b) + (ke * kt)];

tf_mech_num = 1;
tf_mech_denom = [Y1, Y2, Y3];

% DC Motor ve Mekanik Alt Sistem TF.
tf_dc = tf(tf_dc_num, tf_dc_denom);
tf_mech = tf(tf_mech_num, tf_mech_denom);

% Tum sistem TF.
total_system = tf_dc * tf_mech;
total_system_feedback = feedback(total_system, 10);

%% Kutuplarin Bulunmasi
poles = pole(total_system);
fprintf("Poles: "); poles_str = sprintf('%.4e ', poles);
disp(poles_str);

%% Basamak Cevabi
figure;
step(10 * total_system_feedback);
title('Step Response');
grid on;

step_info = stepinfo(total_system_feedback);

fprintf("Overshoot: %f percent.\n", step_info.Overshoot);

%% Son Deger Teoremi
syms s;
[num, den] = tfdata(total_system, 'v');
G_s = poly2sym(num, s) / poly2sym(den, s); 
final_value = limit(s * G_s, s, 0); 
final_value_numeric = double(final_value);

%% Yerlesme Zamani Hesabi
step_info = stepinfo(total_system);
settling_time = step_info.SettlingTime;

disp(['Final Value: ', num2str(final_value_numeric) ...
    ,', Settling Time: ', num2str(settling_time), 's.']);

%% Root Locus & PID Design, %1.5 Overshoot 

PO = 1.5 / 100;
zeta = sqrt((log(PO)^2) / (pi^2 + log(PO)^2)); %(YANLIS MI?)
%zeta = -log(PO / 100) / sqrt(pi^2 + (log(PO / 100))^2);

[rlocus_k, poles] = rlocus(total_system);

figure;
rlocus(total_system);
title('Root Locus');
hold on;
sgrid(zeta, []);

% tuned values from pidtool:
kp = 1.38 * 1000; 
ki = 62.1893;
kd = 4.5451e-08;

pid_controller = pid(kp, ki, kd);
pid_controller = pid_controller * total_system;

CLTF_PID = feedback(pid_controller, 1);
figure;

step(10 * CLTF_PID, 0.25);
title('PID Controller');
grid on;

%pidtool(CLTF_PID);

