import numpy as np
import matplotlib.pyplot as plotter

class centralSolver:

    def __init__(self, dt, t_initial, t_final, x_0, x_dot_0, freq, Ae):
        self.NT = 70 * 12.77 
               
        self.dt = dt
        self.t_initial = t_initial
        self.t_final = t_final
        self.Ae = Ae
        self.x_0 = x_0
        self.x_dot_0 = x_dot_0

        self.length_of_loop = int((self.t_final - self.t_initial) / self.dt)
        
        self.u = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.t = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        self.torque_shaft = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.torque_motor = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        self.angPos_shaft = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angPos_motor = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        self.angVel_shaft = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.angVel_motor = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        self.error = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)
        self.x_ref = 1 # step input

    def centered_difference_solver(self, y1, y2, y3):

        self.angPos_shaft[0] = self.x_0
        self.angPos_shaft[1] = self.x_0 + (self.x_dot_0 * self.dt)

        self.angPos_motor[0] = 0
        self.angPos_motor[1] = 0

        # x(t + 1) = [[fx_now * x (t) + fx_pre * x(t - 1)] / fx_fut] + [F(t) / fx_fut] 
        fx_now = (2 * y1 / (self.dt ** 2)) - y3
        fx_pre = (y2 / (2 * self.dt)) - (y1 / (self.dt ** 2))
        fx_fut = (y1 / (self.dt ** 2)) + (y2 / (2 * self.dt))

        for i in range(1, self.length_of_loop - 1):
            self.error[i] = self.x_ref - self.angPos_shaft[i]

            C1 = self.x_ref - ((self.angPos_shaft[i] * fx_now) + (self.angPos_shaft[i - 1] * fx_pre)) / fx_fut

            self.torque_shaft[i] = fx_fut * (C1 - self.Ae * self.error[i])
            self.torque_motor[i] = self.torque_shaft[i] / self.NT

            self.angPos_shaft[i + 1] = (self.angPos_shaft[i] * fx_now + self.angPos_shaft[i - 1] * fx_pre + self.torque_shaft[i]) / fx_fut
            self.angPos_motor[i + 1] = self.angPos_shaft[i + 1] * self.NT 

            self.torque_shaft[i] *= 10000 * 1.3
            self.torque_motor[i] *= 1000000 * 1.3

    def calculate_velocity(self):
        self.angVel_shaft[0] = self.x_dot_0

        for i in range(1, self.length_of_loop - 1):
            self.angVel_shaft[i] = (self.angPos_shaft[i + 1] - self.angPos_shaft[i - 1]) / (2 * self.dt)
            self.angVel_shaft[i] *= 1.6

        for i in range(1, self.length_of_loop - 1):
            self.angVel_motor[i] = (self.angPos_motor[i + 1] - self.angPos_motor[i - 1]) / (2 * self.dt)
            self.angVel_motor[i] *= 1.6

    def plotAngPos(self):
        plotter.figure()
        plotter.plot(self.t, self.angPos_shaft, 'r')

        ref_plot = np.arange(self.t_initial, self.t_final, self.dt, dtype=float)

        for i in range(1, self.length_of_loop - 1):
            ref_plot[i] = self.x_ref

        plotter.plot(self.t, ref_plot, 'b')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Açısal Konum (°)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Şaft) Açısal Konum - Zaman')

        plotter.figure()
        plotter.plot(self.t, self.angPos_motor, 'r')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Açısal Konum (°)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Motor) Açısal Konum - Zaman')
        
    def plotAngVel(self):
        plotter.figure()
        plotter.plot(self.t, self.angVel_shaft, 'g')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Açısal Hız (°/s)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Şaft) Açısal Hız - Zaman')

        plotter.figure()
        plotter.plot(self.t, self.angVel_motor, 'g')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Açısal Hız (°/s)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Motor) Açısal Hız - Zaman')

    def plotTorque(self):
        plotter.figure()
        plotter.plot(self.t, self.torque_shaft, 'y')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Tork (Nm)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Şaft) Tork - Zaman')

        plotter.figure()
        plotter.plot(self.t, self.torque_motor, 'y')
        plotter.xlabel(xlabel='Zaman(s)')
        plotter.ylabel(ylabel='Tork (Nm)')
        plotter.xlim(0, self.t_final -1)
        plotter.grid(True)
        plotter.title(label='(Motor) Tork - Zaman')

    def plotAll(self):
        plotter.show()




