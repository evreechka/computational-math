import matplotlib.pyplot as plt
import numpy as np

import console_utils


def get_koeff(x, y):
    # delta_ai = (a_i-a_i-1)/hi
    h = [0]
    a = y
    delta_ai = [0]
    for i in range(1, len(x)):
        h.append(x[i] - x[i - 1])
        delta_ai.append((a[i] - a[i - 1]) / h[i])
    alpha = [0] * len(x)
    beta = [0] * len(x)
    alpha[1] = -h[2] / (2 * (h[1] + h[2]))
    beta[1] = (3 * (delta_ai[2] - delta_ai[1])) / (2 * (h[2] + h[1]))
    for i in range(3, len(x)):
        alpha[i - 1] = - h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * alpha[i - 2])
        beta[i - 1] = (3 * delta_ai[i] - 3 * delta_ai[i - 1] - h[i - 1] * beta[i - 2]) / (
                2 * h[i - 1] + 2 * h[i] + h[i - 1] * alpha[i - 2])
    c = [0] * len(x)
    for i in range(len(x) - 1, 1, -1):
        c[i - 1] = alpha[i - 1] * c[i] + beta[i - 1]
    b = [0]
    d = [0]
    for i in range(1, len(x)):
        b.append(delta_ai[i] + (2 * c[i] + c[i - 1]) * h[i] / 3)
        d.append((c[i] - c[i - 1]) / (3 * h[i]))
    return a, b, c, d


def calculate_interpolation(x_values, a, b, c, d, x):
    interpolation_values = []
    index = 1
    for x_i in x_values:
        while x_i > x[index]:
            if index == len(x) - 1:
                break
            index += 1
        interpolation_values.append(
            a[index] + b[index] * (x_i - x[index]) + c[index] * (x_i - x[index]) ** 2 + d[index] * (
                    x_i - x[index]) ** 3)
    return interpolation_values


def show_graphics(a, b, c, d, x, y, function):
    user_points = []
    step = (x[len(x) - 1] - x[0]) / 1000
    x_values = np.arange(x[0], x[len(x) - 1], step)
    y_values = []
    for x_i in x_values:
        y_values.append(function(x_i))
    interpolation_values = calculate_interpolation(x_values, a, b, c, d, x)
    if x[0] <= 0:
        left = x[0] - 1
    else:
        left = 0
    if x[len(x) - 1] >= 0:
        right = x[len(x) - 1] + 1
    else:
        right = 0
    while True:
        plt.figure(figsize=(8, 8))
        plt.axis([left, right, -10, 10])
        plt.xticks(np.arange(left, right, (x[len(x) - 1] - x[0]) / 5))
        plt.hlines(0, left, right, colors='black')
        plt.vlines(0, -10, 10, colors='black')
        plt.plot(x_values, y_values, label='Текущая функция', c='r', linewidth=4)
        plt.plot(x_values, interpolation_values, label='Интерполяция', c='y', linewidth=2)
        for i in range(0, len(user_points) - 1):
            plt.scatter(user_points[i], user_points[i + 1], c='c', s=50)
        plt.grid(True)
        plt.legend(loc=0)
        plt.show()
        close = console_utils.close_application()
        if close == '2':
            return
        new_x = console_utils.read_point(x[0], x[len(x) - 1])
        for i in range(1, len(x)):
            if x[i - 1] <= new_x < x[i]:
                new_y = a[i] + b[i] * (new_x - x[i]) + c[i] * (new_x - x[i]) ** 2 + d[i] * (
                        new_x - x[i]) ** 3
                user_points.append(new_x)
                user_points.append(new_y)
                print('Значение интерполяции в х = ' + str(new_x) + ': y = ' + str(new_y))
