import numpy as np


def cells_method(step_num, a, b, c, d, f):
    step_x = (b - a) / step_num
    step_y = (d - c) / step_num
    x = np.linspace(a, b, step_num)
    y = np.linspace(c, d, step_num)
    I = 0
    for i in range(1, len(x)):
        for j in range(1, len(x)):
            x_i = (x[i] + x[i - 1]) / 2
            y_i = (y[j] + y[j - 1]) / 2
            I += step_x * step_y * f(x_i, y_i)
    return I


def trapeze_method(step_num, a, b, c, d, f):
    step_x = abs(b - a) / step_num
    step_y = abs(d - c) / step_num
    x = np.linspace(a, b, step_num)
    y = np.linspace(c, d, step_num)
    F_y = []
    for i in range(0, len(y)):
        integral_sum = 0
        for j in range(0, len(x)):
            if j == 0 or j == len(x):
                q = 1 / 2
            else:
                q = 1
            integral_sum += q * f(x[j], y[i]) * step_x
        F_y.append(integral_sum)
    integral = 0
    for i in range(0, len(F_y)):
        if i == 0 or i == len(F_y):
            q = 1 / 2
        else:
            q = 1
        integral += q * F_y[i] * step_y
    return integral


def middle_rectangle_method(step_num, a, b, c, d, f):
    step_x = abs(b - a) / step_num
    step_y = abs(d - c) / step_num
    x = np.linspace(a, b, step_num)
    y = np.linspace(c, d, step_num)
    F_y = []
    for i in range(0, len(y)):
        integral_sum = 0
        for j in range(0, len(x) - 1):
            integral_sum += f(x[j] + step_x / 2, y[i]) * step_x
        F_y.append(integral_sum)
    integral = 0
    for i in range(0, len(F_y)):
        integral += F_y[i] * step_y
    return integral


def left_rectangle_method(step_num, a, b, c, d, f):
    step_x = abs(b - a) / step_num
    step_y = abs(d - c) / step_num
    x = np.linspace(a, b, step_num)
    y = np.linspace(c, d, step_num)
    F_y = []
    for i in range(0, len(y)):
        integral_sum = 0
        for j in range(0, len(x)):
            integral_sum += f(x[j], y[i]) * step_x
        F_y.append(integral_sum)
    integral = 0
    for i in range(0, len(F_y)):
        integral += F_y[i] * step_y
    return integral


def right_rectangle_method(step_num, a, b, c, d, f):
    step_x = abs(b - a) / step_num
    step_y = abs(d - c) / step_num
    x = np.linspace(a, b, step_num)
    y = np.linspace(c, d, step_num)
    F_y = []
    for i in range(0, len(y)):
        integral_sum = 0
        for j in range(0, len(x) - 1):
            integral_sum += f(x[j] + step_x, y[i]) * step_x
        F_y.append(integral_sum)
    integral = 0
    for i in range(0, len(F_y)):
        integral += F_y[i] * step_y
    return integral


def rule_runge(step_num, accuracy, a, b, c, d, f, integral_method):
    I_0 = integral_method(step_num, a, b, c, d, f)
    step_num *= 2
    I_1 = integral_method(step_num, a, b, c, d, f)
    delta = abs(I_1 - I_0) / 3
    while delta > accuracy:
        I_0 = I_1
        step_num *= 2
        I_1 = integral_method(step_num, a, b, c, d, f)
        delta = abs(I_1 - I_0) / 3
        if step_num > 400:
            return step_num
    return step_num
