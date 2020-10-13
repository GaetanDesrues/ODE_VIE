import numpy as np

#
# A problem is defined as the right side of the ODE written in the normal form
#
# Signature:
# def problem(t, y, *params):
#     return f(t, y(t), params)
#
# Example: let's consider the ODE y'(t) = Ay^2 + Bt
# Then the associated problem is
# def myODE(t, y, A, B):
#     return A*y**2 + B*t
# and called in the main program as
# A, B = np.pi, -52.2
# params = [A, B]
# myODE(t, y, *params)
#



def Exponential(t, y, k):
    """
    Default params: params = [1]
    """
    # TODO


def LoktaVolterra(t, y, k1, k2, a1, a2):
    """
    Default params: params = [1, 1, 1, 0.2]
    """
    # TODO


def Michell_Schaeffer(t, y, tin, tout, topen, tclose, vgate, JStim, T_stim):
    """
    Default params: params = [0.3, 6, 120, 150, 0.13, periodic_stimulation, 500]
    
    # Stimulation
    t_stim, vstim = 0.1, 1
    def periodic_stimulation(t, T_stim):
        return vstim if 0 <= t % T_stim <= t_stim else 0
    """
    # TODO