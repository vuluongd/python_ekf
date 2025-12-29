import numpy as np

class imu:
    def __init__(self, bias):
        self.bias = bias
        self.vel = np.zeros(2)
        self.pos = np.zeros(2)


    def update(self, acc, dt):
        acc_m = acc + self.bias * np.random.randn(2)
        self.vel += acc_m * dt
        self.pos += self.vel * dt + 0.5 * acc_m *dt**2
        return acc_m
    
        
        