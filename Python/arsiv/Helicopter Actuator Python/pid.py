
class PID_Controller:
    def __init__(self, kp, ki, kd, tau, lim_min, lim_max, dt):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.tau = tau

        self.lim_min = lim_min
        self.lim_max = lim_max

        self.dt = dt

        self.integrator = 0.0
        self.prevError = 0.0
        self.differentiator = 0.0
        self.prevMeasurment = 0.0

        self.out = 0.0
    
    def Update(self, setpoint, measurement):
        # Calculate error:
        error = setpoint - measurement

        # Proportional
        proportional = self.kp * error

        # Integrator
        self.integrator = self.integrator + (0.5 * self.ki * (error - self.prevError))

        # Derivative 
        self.differentiator = (2 * self.kd) * (measurement - self.prevMeasurment) + (2 * self.tau * self.dt * self.differentiator) 
        self.differentiator = self.differentiator / (2 * self.tau * self.dt)

        # Integrator Limits
        if (self.lim_max > proportional):
            lim_maxInt = self.lim_max - proportional
        else:
            lim_maxInt = 0.0

        if (self.lim_min < proportional):
            lim_minInt = self.lim_min - proportional
        else:
            lim_minInt = 0.0

        # Integrator Anti-Windup
        if (self.integrator > lim_maxInt):
            self.integrator = lim_maxInt

        elif (self.integrator < lim_minInt):
            self.integrator = lim_minInt

        # Output calculation
        self.out = proportional + self.integrator + self.differentiator

        # Check output limits
        if (self.out > self.lim_max):
            self.out = self.lim_max

        elif (self.out < self.lim_min):
            self.out = self.lim_min  

        self.prevError = error
        self.prevMeasurment = measurement

        return self.out

