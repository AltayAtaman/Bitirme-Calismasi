import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class solver:
    def __init__(self, dt, t_initial, t_final, systemCoef_a, systemCoef_u, x_initial):
        self.dt = dt
        self.t_initial = t_initial
        self.t_final = t_final
        self.systemCoef_a = systemCoef_a
        self.systemCoef_u = systemCoef_u
        self.x = np.arange(self.t_initial, self.t_final, self.dt)
        self.u = np.arange(int((t_final - t_initial) / dt))
        self.t = np.arange(t_initial, t_final, dt) 
        self.x_initial = x_initial
        self.x[0] = self.x_initial

        for i in range (0, int((t_final - t_initial) / dt)):
            self.u[i] = i

    def forwardDiffrence(self):

        for k in range(0, int(self.t_final / self.dt) - 1):
            self.x[k + 1] = self.x[k] + self.dt * (self.systemCoef_a * self.x[k] + self.systemCoef_u * self.u[k])
            print("t = {0}, x = {1}".format(self.t[k], self.x[k]))

    def backwardDiffrence(self):

        for k in range(1, int(self.t_final / self.dt)):
            self.x[k] = self.x[k - 1] + self.dt * (self.systemCoef_a  * self.x[k - 1] + self.systemCoef_u * self.u[k - 1])
            print("t = {0}, x = {1}".format(self.t[k], self.x[k]))

    def centeredDiffrence(self):
        self.x[1] = self.x_initial + (self.dt * 2 * (self.systemCoef_a * self.x[0] + self.systemCoef_u * self.u[0]))

        for k in range(1, int(self.t_final / self.dt) - 1):
            self.x[k + 1] = self.x[k - 1] + 2 * self.dt * (self.systemCoef_a  * self.x[k - 1] + self.systemCoef_u * self.u[k - 1])
            print("t = {0}, x = {1}".format(self.t[k], self.x[k]))

    def plot(self, color, xlabel='x', ylabel='y', figure_title='title'):
        plt.figure()
        plt.plot(self.t, self.x, color, marker = '')
        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
        plt.grid(True)
        plt.title(figure_title)        
        plt.show(block = False)





 