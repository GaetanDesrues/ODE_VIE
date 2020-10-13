import numpy as np


def Exponential(t, y, k):
    """
    Default params: params = [1]
    """
    return k * y


def LoktaVolterra(t, y, k1, k2, a1, a2):
    """
    Default params: params = [1, 1, 1, 0.2]
    """
    dy1 = a1 * y[0] * (1 - y[1] / k2)
    dy2 = -a2 * y[1] * (1 - y[0] / k1)
    
    return np.array([dy1, dy2])


def Michell_Schaeffer(t, y, tin, tout, topen, tclose, vgate, JStim, T_stim):
    """
    Default params: params = [0.3, 6, 120, 150, 0.13, periodic_stimulation, 500]
    
    # Stimulation
    t_stim, vstim = 0.1, 1
    def periodic_stimulation(t, T_stim):
        return vstim if 0 <= t % T_stim <= t_stim else 0
    """
    v, h = y

    # 2 currents
    JIn = lambda v, h: h * v ** 2 * (1 - v) / tin  # (2)
    JOut = lambda v: -v / tout  # (3)

    # System of equations
    dvdt = JIn(v, h) + JOut(v) + JStim(t, T_stim)  # (1)
    dhdt = (1 - h) / topen if v < vgate else -h / tclose  # (4)
    
    return np.array([dvdt, dhdt])