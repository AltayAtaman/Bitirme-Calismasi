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

%% Kutuplarin Bulunmasi
poles = pole(total_system);
fprintf("Poles: "); poles_str = sprintf('%.4e ', poles);
disp(poles_str);

%% Basamak Cevabi
figure;
step(10 * total_system);
title('Step Response o');
grid on;

%% Son Deger Teoremi
syms s;
[num, den] = tfdata(open_loop_response, 'v');
G_s = poly2sym(num, s) / poly2sym(den, s); 
final_value = limit(s * G_s, s, 0); 
final_value_numeric = double(final_value);

%% Yerlesme Zamani Hesabi
step_info = stepinfo(total_system);
settling_time = step_info.SettlingTime;

disp(['Final Value: ', num2str(final_value_numeric) ...
    ,', Settling Time: ', num2str(settling_time), 's.']);
