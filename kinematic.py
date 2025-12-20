import numpy as np
def trajectory(p_start, p_end, t, T):
    tau = t/T
    s = 10*tau**3 - 15*tau**4 + 6*tau**5
    