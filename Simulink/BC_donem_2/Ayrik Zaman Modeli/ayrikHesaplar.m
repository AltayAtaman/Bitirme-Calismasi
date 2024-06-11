%% Ayrik Kontrolcu Girdileri:

dt = 0.1;
Ae = 0.5;
x_0 = 0; x_0_dot = 0;

fx_now = (2 .* y1 / (dt .^ 2)) - y3;
fx_pre = (y2 / (2 .* dt)) - (y1 / (dt .^ 2));
fx_fut = (y1 / (dt .^ 2)) + (y2 / (2 .* dt));

h_fut_2 = z1 / dt^3;
h_fut = (z2 / dt^2) + (z3 / (2 * dt)) - ((3 * z1) / dt^3);
h_now = ((3 * z1) / dt^3) - ((2 * z2) / dt^2);
h_prev = (z2 / dt^2) - (z3 / (2 * dt)) - (z1 / dt^3);

constants = [fx_now
             fx_pre
             fx_fut
             x_0
             x_0_dot
             Ae
             N1
             N2
             N3];       