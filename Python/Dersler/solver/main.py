from discreteFunctions import solver  
import time

forwardDiff = solver(dt = 0.001, t_initial = 0.0, t_final = 1.0, systemCoef_a = -3, systemCoef_u = 1, x_initial = 10)
#backwardDiff = solver(dt = 0.001, t_initial = 0.0, t_final = 1.0, systemCoef_a = -3, systemCoef_u = 1, x_initial = 10)
#centeredDiff = solver(dt = 0.001, t_initial = 0.0, t_final = 1.0, systemCoef_a = -3, systemCoef_u = 1, x_initial = 10)

forwardDiff.forwardDiffrence()
#backwardDiff.backwardDiffrence()
#centeredDiff.centeredDiffrence()

forwardDiff.plot(color='r', figure_title='Forward Diffrence')
#backwardDiff.plot(color='b', figure_title='Backward Diffrence')
#centeredDiff.plot(color='g', figure_title='Centered Diffrence')

#equation = solver(dt = 0.001, t_initial = 0.0, t_final = 1.0, systemCoef_a = -3, x_initial = 10)
#equation.linearize(method='forward')
#equation.plot(color='g', figure_title='Linearized by Forward Diff.')

while (input() == 0):
    time.sleep()


