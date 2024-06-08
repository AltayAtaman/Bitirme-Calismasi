from solver import centralSolver
from system import actuatorSystem
import time

if __name__ == "__main__":
    actuator_f = actuatorSystem(kT = 0.17, cM = 0.022)

    solver_f = centralSolver(dt=0.1, t_initial = 0.0, t_final = 10.0, 
                                    x_0 = 0, x_dot_0 = 0, 
                                    freq = 0.5, Ae = 0.2) 
    
    solver_f.centered_difference_solver(y1 = actuator_f.Y1, y2 = actuator_f.Y2, y3 = actuator_f.Y3)

    solver_f.calculate_velocity()

    #solver_f.plotAngPos()
    solver_f.plotTorque()
    #solver_f.plotAngVel()
    solver_f.plotAll()

    print('Simulation completed')

