%% Final Value Theorem:
total_system = tf(kt, [L*Y1, L*Y2 + R*Y1, L*Y3 + R*Y2 + kt*ke, R*Y3]);
system_input = tf(1, [1, 0]); 

open_loop_response = total_system * system_input;

% Apply final value theorem
syms s;
[num, den] = tfdata(open_loop_response, 'v');
G_s = poly2sym(num, s) / poly2sym(den, s); 
final_value = limit(s * G_s, s, 0); 
final_value_numeric = double(final_value);

% Compute and display the settling time
step_info = stepinfo(total_system);
settling_time = step_info.SettlingTime;

disp(['Final Value: ', num2str(final_value_numeric) ...
    ,', Settling Time: ', num2str(settling_time), 's.']);
