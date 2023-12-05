
class actuatorSystem:
    def __init__(self):
        # Reduction ratios
        self.N1 = 1; self.N2 = 70; self.N3 = 12.77; self.N4 = 8.25

        # System parameters
        self.kT = 0.17 # (n.m)/(degree)
        self.cM = 0.022 # (n.m)/(degree*sec)

        # System shape/material parameters
        self.rhoM = 2700 # for aluminium
        self.rhoMSG = 2700
        self.rhoWG = 2700
        self.rhoDSP = 2700
        self.rhoDSG = 2700
        self.rhoSG = 2700

        self.mM = 47.5 * 10e-3  # kg
        self.mMSG = 17.5 * 10e-3  # kg
        self.mWG = 100 * 10e-3  # kg
        self.mDSP = 325 * 10e-3 # kg
        self.mDSG = 89 * 10e-3  # kg
        self.mSG = 180 * 10e-3  # kg

        self.rM = 5.25 * 10e-3  # m
        self.rMSG = 5.25 * 10e-3  # m
        self.rWG = 5.25 * 10e-3  # m
        self.rDSP = 25 * 10e-3  # m
        self.rDSG = 49.8 * 10e-3 # m
        self.rSG = 59.4 * 10e-3 # m

        # System inertias
        self.jM = 1/2*self.mM*((self.rM)^2)
        self.jMSG = 1/2*self.mMSG*((self.rMSG)^2)
        self.jWG = 1/2*self.mWG*((self.rWG)^2)
        self.jDSP = 1/2*self.mDSP*((self.rDSP)^2)
        self.jDSG = 1/2*self.mDSG*((self.rDSG)^2)
        self.jSG = 1/2*self.mSG*((self.rSG)^2)

        # System efficiency
        self.etaWG = 0.3

        # X values
        self.x1 = self.kT/(self.N1*self.N2*self.N3*self.N4)
        self.x2 = self.jSG/((self.N1*self.N2*self.N3*self.N4)^2)
        self.x3 = self.jDSG/((self.N1*self.N2*self.N3)^2)
        self.x4 = self.cM/(self.N1*self.N2)
        self.x5 = self.jDSP/((self.N1*self.N2)^2)
        self.x6 = self.jWG/(self.N1^2)
        self.x7 = self.jM + self.jMSG

        # Y values
        self.Y1 = self.x7 + self.x6 + (self.x5 + self.x3 + self.x2)/(self.etaWG)
        self.Y2 = self.x4/(self.etaWG)
        self.Y3 = self.x1/(self.etaWG)

        return [self.Y1, self.Y2, self.Y3]
