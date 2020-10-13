# A method returns the solution at time t + dt from the solution y at time t
# f represents the problem to solve

def EulerExplicite(t, y, h, f, params):
    # TODO: implement the forward euler method


def RungeKutta4(t, y, h, f, params):
    f1 = f(t, y, *params)
    f2 = f(t + 0.5 * h, y + h * 0.5 * f1, *params)
    f3 = f(t + 0.5 * h, y + h * 0.5 * f2, *params)
    f4 = f(t + h, y + h * f3, *params)
    return y + h * (f1 + 2 * f2 + 2 * f3 + f4) / 6
