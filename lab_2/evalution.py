import matplotlib.pyplot as plt
from numpy import arange, meshgrid
from sympy import *


def get_diff_max(bitness, list_koef, a, b):
    x = symbols('x')
    curr_fun = x ** bitness * list_koef[0]
    for i in range(1, bitness):
        curr_fun += x ** (bitness - i) * list_koef[i]
    return maximum(curr_fun.diff(x), x, Interval(a, b))


def graph_eval(function, bitness, list_koef):
    interval = arange(-25, 25, 0.01)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(interval, function(interval, bitness, list_koef))
    ax.axis([-25, 25, 0, 100])
    plt.show()


def graph_res_eval(function, x_chord, x_iterate, bitness, list_koef):
    interval = arange(-25, 25, 0.01)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(interval, function(interval, bitness, list_koef))
    ax.axis([-25, 25, -100, 100])
    if x_chord is not None:
        ax.scatter(x_chord, 0, c='r')
    if x_iterate is not None:
        ax.scatter(x_iterate, 0, c='g')
    plt.show()


def method_iterations(a, b, eps, f, list_koef, bitness):
    iterations = 1
    if f(a, bitness, list_koef) == 0:
        return a
    if f(b, bitness, list_koef) == 0:
        return b
    lambda0 = 1 / get_diff_max(bitness, list_koef, a, b)
    x_curr = a - f(a, bitness, list_koef) * lambda0
    while abs(x_curr - a) >= eps:
        a = x_curr
        iterations += 1
        x_curr = a - f(a, bitness, list_koef) * lambda0
    print('Количество итераций: ' + str(iterations))
    return x_curr


def method_chord(a, b, eps, f, list_koef, bitness):
    if f(a, bitness, list_koef) == 0:
        return a
    if f(b, bitness, list_koef) == 0:
        return b
    x_curr = a
    iterations = 1
    x_pred = x_curr
    x_curr = (a * f(b, bitness, list_koef) - b * f(a, bitness, list_koef)) / (
            f(b, bitness, list_koef) - f(a, bitness, list_koef))
    if f(a, bitness, list_koef) * f(x_curr, bitness, list_koef) < 0:
        b = x_curr
    else:
        a = x_curr
    while abs(x_curr - x_pred) >= eps:
        iterations += 1
        x_pred = x_curr
        x_curr = (a * f(b, bitness, list_koef) - b * f(a, bitness, list_koef)) / (
                f(b, bitness, list_koef) - f(a, bitness, list_koef))
        if f(a, bitness, list_koef) * f(x_curr, bitness, list_koef) < 0:
            b = x_curr
        else:
            a = x_curr
    print('Количество итераций: ' + str(iterations))
    return x_curr


def get_res_eval(function, bitness, list_koef):
    graph_eval(function, bitness, list_koef)
    x_chord = 0
    x_iterate = 0
    choice1 = '0'
    choice2 = '0'
    while True:
        a = float(input('Введите левую границу промежутка: '))
        b = float(input('Введите правую границу промежутка: '))
        if function(a, bitness, list_koef) * function(b, bitness, list_koef) <= 0:
            eps = float(input('Введите точность: '))
            x_chord = method_chord(a, b, eps, function, list_koef, bitness)
            print('Корень уравнения, полученный методом хорд: х=' + str(x_chord))
            break
        print('f(a)=' + str(function(a, bitness, list_koef)))
        print('f(b)=' + str(function(b, bitness, list_koef)))
        choice1 = input('Данный промежуток не содержит решения уравнения! '
                        'Уравнение может не иметь корней, хотите ввести промежуток еще раз?(1-да, 2-нет)')
        if choice1 == '2':
            break

    while True:
        a = float(input('Введите левую границу промежутка: '))
        b = float(input('Введите правую границу промежутка: '))
        if function(a, bitness, list_koef) * function(b, bitness, list_koef) <= 0:
            eps = float(input('Введите точность: '))
            x_iterate = method_iterations(a, b, eps, function, list_koef, bitness)
            print('Корень уравнения, полученный методом простых итераций: х=' + str(x_iterate))
            break
        print('f(a)=' + str(function(a, bitness, list_koef)))
        print('f(b)=' + str(function(b, bitness, list_koef)))
        choice2 = input('Данный промежуток не содержит решения уравнения! '
                        'Уравнение может не иметь корней, хотите ввести промежуток еще раз?(1-да, 2-нет)')
        if choice2 == '2':
            break
    if choice1 == '2' and choice2 == '2':
        graph_res_eval(function, None, None, bitness, list_koef)
    elif choice1 != '2' and choice2 == '2':
        graph_res_eval(function, x_chord, None, bitness, list_koef)
    elif choice1 == '2' and choice2 != '2':
        graph_res_eval(function, None, x_iterate, bitness, list_koef)
    else:
        print('Разница в значениях решений: ' + str(abs(x_chord - x_iterate)))
        graph_res_eval(function, x_chord, x_iterate, bitness, list_koef)
