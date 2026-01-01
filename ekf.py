import numpy as np 

class EKF:
    def __init__(self, Q, R):
        self.X = np.zeros(4)
        self.P = np.eye(4)
        self.Q = Q
        self.R = R

    def predict(self, acc, dt):
        F = np.array([1,0,dt,0],
                     [0,1,0,dt],
                     [0,0,1,0],
                     [0,0,0,1])
        B = np.array([0.5*dt**2,0],
                     [0,0.5*dt**2],
                     [dt,0],
                     [0,dt])
        self.X = F @ self.X + B @ acc
        self.P = F @ self.P @ F.T + self.Q

    def update(self, z, station):
        dx = self.X[0] - station[0]
        dy = self.Y[1] - station[1]

        
        
