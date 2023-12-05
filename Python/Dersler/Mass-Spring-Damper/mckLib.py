import numpy as np
import matplotlib.pyplot as plotter

class mass_damper_spring:

    def __init__(self, dt, t_initial, t_final, x_0, x_dot_0, force):
        self.dt = dt
        self.t_initial = t_initial
        self.t_final = t_final

        self.x_0 = x_0
        self.x_dot_0 = x_dot_0
        self.length_of_loop = int((self.t_final - self.t_initial) / self.dt)
        
        self.u = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        for i in range(0, self.length_of_loop):
            self.u[i] = force

        self.t = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angPos = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angVel = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

    def centered_difference_solver(self):

        self.angPos[0] = self.x_0
        self.angPos[1] = self.x_0 + (self.x_dot_0 * self.dt)

        # x(t + 1) = [[fx_now * x (t) + fx_pre * x(t - 1)] / fx_fut] + [F(t) / fx_fut] 
        self.fx_now = (2 / (self.dt ** 2)) - 2
        self.fx_pre = (3 / (2 * self.dt)) - (1 / (self.dt ** 2))
        self.fx_fut = (1 / (self.dt ** 2)) + (3 / (2 * self.dt))

        for i in range(1, self.length_of_loop - 1):
            self.angPos[i + 1] = ((self.angPos[i] * self.fx_now) + (self.angPos[i - 1] * self.fx_pre)) / self.fx_fut + self.u[i] / self.fx_fut
            print(self.angPos[i - 1])

    def calculate_velocity(self):
        self.angVel[0] = self.x_dot_0

        for i in range(1, self.length_of_loop - 1):
            self.angVel[i] = (self.angPos[i + 1] - self.angPos[i - 1]) / (2 * self.dt)


    def plotAngPos(self, xlabel, ylabel, title):
        plotter.figure()
        plotter.plot(self.t, self.angPos, 'r')
        plotter.xlabel(xlabel)
        plotter.ylabel(ylabel)
        plotter.grid(True)
        plotter.title(title)
        plotter.show()

    def plotAngVel(self, xlabel, ylabel, title):
        plotter.figure()
        plotter.plot(self.t, self.angVel, 'r')
        plotter.xlabel(xlabel)
        plotter.ylabel(ylabel)
        plotter.grid(True)
        plotter.title(title)
        plotter.show()

