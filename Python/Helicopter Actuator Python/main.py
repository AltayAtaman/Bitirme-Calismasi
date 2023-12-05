from solver import centralSolver
from system import actuatorSystem
import time

if __name__ == "__main__":

    actuator_f = actuatorSystem(kT = 0.17, cM = 0.022)

    solver_f = centralSolver(dt=0.1, t_initial = 0.0, t_final = 10.0, 
                                    x_0 = 2, x_dot_0 = 0, 
                                    torque_input = 0.1, Ae = 0.5) 
    
    solver_f.centered_difference_solver(y1 = actuator_f.Y1, y2 = actuator_f.Y2, y3 = actuator_f.Y3)

    solver_f.calculate_velocity()

    solver_f.plotAngPos(xlabel='Time(s)', ylabel='Angular Position', title='Ang. Pos / Time')
    solver_f.plotForce(xlabel='Time(s)', ylabel='Torque', title='Torque / Time')
    solver_f.plotAngVel(xlabel='Time(s)', ylabel='Angular Velocity', title='Angular Velocity / Time')
    solver_f.plotAll()

    print('Simulation completed')

