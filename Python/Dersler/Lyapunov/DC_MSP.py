from mckLib import mass_damper_spring 
import time

if __name__ == "__main__":

    mck_system = mass_damper_spring(dt=0.1, t_initial = 0.0, t_final = 10.0, 
                                    x_0 = 2, x_dot_0 = 0, 
                                    force_input = 0.1, Ae = 0.5) 
    
    mck_system.centered_difference_solver()
    mck_system.plotAngPos(xlabel='Time(s)', ylabel='Displecement(m)', title='Ang. Pos/Time')
    mck_system.plotForce(xlabel='Time(s)', ylabel='Force(N)', title='Force/Time')
    #mck_system.calculate_velocity()
    #mck_system.plotAngVel(xlabel='Time(s)', ylabel='Velocity(m)', title='Mass-Damper-Spring')

    print('Simulation completed')


