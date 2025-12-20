import numpy as np

def dme_measurement(pos_station, pos_uav, r_max, noise_std):
    z= []
    for s in pos_station:
        d = np.linalg.norm(pos_uav - s)
        if d < r_max :
            d += noise_std * np.random.randn()
            z.append(d)
        else:
            z.append(np.nan)
    return z
        
