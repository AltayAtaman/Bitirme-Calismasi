
class actuatorSystem:
    def __init__(self, kT, cM):
        # Reduction ratios
        self.N1 = 1; self.N2 = 70; self.N3 = 12.77

        # System parameters
        self.kT = kT # (n.m)/(degree)
        self.cM = cM # (n.m)/(degree*sec)

        # System shape/material parameters
        self.rhoM = 1.220 # for aluminium
        self.rhoMSG = 1.220
        self.rhoWG = 1.220
        self.rhoDSP = 1.220
        self.rhoSG = 1.220

        self.mM = 47.5 * 0.001  # kg
        self.mMSG = 17.5 * 0.001  # kg
        self.mWG = 100 * 0.001  # kg
        self.mDSP = 325 * 0.001 # kg
        self.mSG = 180 * 0.001  # kg

        self.rM = 5.25 * 0.001  # m
        self.rMSG = 5.25 * 0.001  # m
        self.rWG = 5.25 * 0.001  # m
        self.rDSP = 25 * 0.001  # m
        self.rSG = 59.4 * 0.001 # m

        # System inertias
        self.jM = 0.5 * self.mM * ((self.rM) ** 2)
        self.jMSG = 0.5 * self.mMSG * ((self.rMSG) ** 2)
        self.jWG = 0.5 * self.mWG * ((self.rWG) ** 2)
        self.jDSP = 0.5 * self.mDSP * ((self.rDSP) ** 2)
        self.jSG = 0.5 * self.mSG * ((self.rSG) ** 2)

        # System efficiency
        self.etaWG = 0.3

        # X values
        self.x1 = self.kT / (self.N1 * self.N2 * self.N3)
        self.x2 = self.jSG / ((self.N1 * self.N2 * self.N3) ** 2)
        self.x3 = self.cM / (self.N1 * self.N2)
        self.x4 = self.jDSP / ((self.N1 * self.N2) ** 2)
        self.x5 = self.jWG / (self.N1 ** 2)
        self.x6 = self.jM + self.jMSG

        # Y values
        self.Y1 = self.x6 + self.x5 + (self.x4 + self.x2) / (self.etaWG)
        self.Y2 = self.x3 / (self.etaWG)
        self.Y3 = self.x1 / (self.etaWG)
        print("Y VALUES"); print(self.Y1); print(self.Y2); print(self.Y3); print("--")
