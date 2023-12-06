import numpy as np
import matplotlib.pyplot as plotter

class centralSolver:

    def __init__(self, dt, t_initial, t_final, x_0, x_dot_0, freq, Ae):
               
        self.dt = dt
        self.t_initial = t_initial
        self.t_final = t_final
        self.Ae = Ae
        self.x_0 = x_0
        self.x_dot_0 = x_dot_0

        self.length_of_loop = int((self.t_final - self.t_initial) / self.dt)
        
        self.u = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        self.Torque = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.t = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angPos = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angVel = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.error = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        #self.x_ref = 5 + np.sin(2*np.pi*freq*self.t)
        self.x_ref = 10

    def centered_difference_solver(self, y1, y2, y3):

        self.angPos[0] = self.x_0
        self.angPos[1] = self.x_0 + (self.x_dot_0 * self.dt)

        # x(t + 1) = [[fx_now * x (t) + fx_pre * x(t - 1)] / fx_fut] + [F(t) / fx_fut] 
        fx_now = (2 * y1 / (self.dt ** 2)) - y3
        fx_pre = (y2 / (2 * self.dt)) - (y1 / (self.dt ** 2))
        fx_fut = (y1 / (self.dt ** 2)) + (y2 / (2 * self.dt))

        for i in range(1, self.length_of_loop - 1):
            self.error[i] = self.x_ref - self.angPos[i]

            C1 = self.x_ref - ((self.angPos[i] * fx_now) + (self.angPos[i - 1] * fx_pre)) / fx_fut

            self.Torque[i] = fx_fut * (C1 - self.Ae * self.error[i])
            print(self.Torque[i])

            self.angPos[i + 1] = (self.angPos[i] * fx_now + self.angPos[i - 1] * fx_pre + self.Torque[i]) / fx_fut
            self.Torque[i] = self.Torque[i] * 1000

            #print(self.angPos[i - 1])

    def calculate_velocity(self):
        self.angVel[0] = self.x_dot_0

        for i in range(1, self.length_of_loop - 1):
            self.angVel[i] = (self.angPos[i + 1] - self.angPos[i - 1]) / (2 * self.dt)


    def plotAngPos(self, xlabel, ylabel, title):
        plotter.figure()
        plotter.plot(self.t, self.angPos, 'r')

        ref_plot = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        for i in range(1, self.length_of_loop - 1):
            ref_plot[i] = self.x_ref

        plotter.plot(self.t, ref_plot, 'b')
        plotter.xlabel(xlabel)
        plotter.ylabel(ylabel)
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(title)
        

    def plotAngVel(self, xlabel, ylabel, title):
        plotter.figure()
        plotter.plot(self.t, self.angVel, 'g')
        plotter.xlabel(xlabel)
        plotter.ylabel(ylabel)
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(title)

    def plotTorque(self, xlabel, ylabel, title):
        plotter.figure()
        plotter.plot(self.t, self.Torque, 'y')
        plotter.xlabel(xlabel)
        plotter.ylabel(ylabel)
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(title)

    def plotAll(self):
        plotter.show()




