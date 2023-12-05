import numpy as np


dt = 0.001

t_initial = 0
t_final = 10.0

length_of_loop = int((t_final - t_initial) / dt)

t = np.arange(t_initial, t_final, dtype=float)

# x(t + 1) = [a * x(t) + b * x(t - 1)] / c

a = (2 / dt * dt) - 2
b = (3 / (2 * dt)) - (1 / (dt * dt)) 
c = (1 / dt * dt) + (3 / (2 * dt))
