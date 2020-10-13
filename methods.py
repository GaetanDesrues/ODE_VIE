def EulerExplicite(t, y, h, f, params):
    return y + h * f(t, y, *params)


def RungeKutta4(t, y, h, f, params):
    f1 = f(t, y, *params)
    f2 = f(t + 0.5 * h, y + h * 0.5 * f1, *params)
    f3 = f(t + 0.5 * h, y + h * 0.5 * f2, *params)
    f4 = f(t + h, y + h * f3, *params)
    return y + h * (f1 + 2 * f2 + 2 * f3 + f4) / 6
