import numpy as np

def trajectory(p_start, p_end, t, T):
    tau = t/T
    s = 10*tau**3 - 15*tau**4 + 6*tau**5
    v = (30*tau**2 - 60*tau**3 + 30*tau**4)/T
    a = (60*tau - 180*tau**2 + 120*tau**3)/T**2

    pos = (p_start - p_end)*s
    vel = (p_start - p_end)*v
    acc = (p_start - p_end)*a 

    return pos, vel, acc





    

