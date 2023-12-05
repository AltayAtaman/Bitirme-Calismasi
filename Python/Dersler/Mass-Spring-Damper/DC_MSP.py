from mckLib import mass_damper_spring 
import time

if __name__ == "__main__":

    mck_system = mass_damper_spring(dt=0.001, t_initial = 0.0, t_final = 10.0, x_0 = 10, x_dot_0 = 5, force=25) # 5:11, video 35
    mck_system.centered_difference_solver()
    mck_system.plotAngPos(xlabel='Time(s)', ylabel='Displecement(m)', title='Mass-Damper-Spring')
    mck_system.calculate_velocity()
    mck_system.plotAngVel(xlabel='Time(s)', ylabel='Velocity(m)', title='Mass-Damper-Spring')

    print('Simulation completed')


