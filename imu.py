import numpy as np

class imu:
    def _init_(self, dt, acc_bias = 0.001, gyro_bias = 0.0001):
        self.dt = dt
        self.g = 9.81

        self.Ba = acc_bias
        self.Bg = gyro_bias

        self.v = np.zeros(2)
        self.p = np.zeros(2)

        self.dv = np.zeros(2)
        self.dp = np.zeros(2)

    def update(self, acc, dtheta):
        dt = self.dt

        a_B = acc + self.Ba 

        self.dv = (
            self.dv 
            + self.Ba * dt
            + self.g * dtheta*dt
            - self.g* self.Bg *dt**2
        )

        self.dp = (
            self.dp 
            + self.dv * dt
            + 0.5 * self.Ba * dt**2
            - 0.5 * self.g * dtheta * dt**2
            - (1/6) * self.g * self.Bg * dt**3
        )

        self.v = (self.v - self.dv) + a_B * dt + self.dv

        self.p = (self.p - self.dp) + (self.v - self.dv)*dt + 0.5*a_B*dt**2

        return self.v, self.p


        
        