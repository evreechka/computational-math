from math import exp


def f1_XY(x, y):
    return - y + 7 * exp(x)


def f1_X(x):
    return (1 + 7 * exp(2 * x) / 2) * exp(-x)


def f2_XY(x, y):
    return x ** 2 + 2 * x + y


def f2_X(x):
    return exp(x) - x ** 2 - 4 * x - 4


def read_function():
    fun_num = 0
    while fun_num == 0:
        try:
            fun_num = int(input('Выберете номер уравнение:'
                                '\n 1. y\' + y - 7 * exp(x) = 0'
                                '\n 2. y\' - (x^2 + 2 * x + y) = 0\n'))
            if fun_num < 1 or fun_num > 2:
                print('Неверный номер уравнения :(')
                fun_num = 0
            else:
                if fun_num == 1:
                    print('x0 = 0; y0 = 4.5')
                    return f1_XY, f1_X, 0, 4.5
                else:
                    print('x0 = 0; y0 = -3')
                    return f2_XY, f2_X, 0, -3
        except ValueError:
            print('Некорректный номер функции')
            fun_num = 0


def read_initial_conditions(x0):
    while True:
        print('Введите конец отрезка:')
        try:
            b = float(input('b = '))
            if b <= x0:
                print('Конец отрезка не может быть меньше x_0')
                continue
            break
        except ValueError:
            print('Неверный формат для b')
    while True:
        print('Введите точность решения:')
        try:
            eps = float(input('eps = '))
            break
        except ValueError:
            print('Неверный формат для eps')
    return b, eps


def close_application():
    continue_add_points = ''
    while continue_add_points != '1' and continue_add_points != '2':
        continue_add_points = input('Хотите посчитать значение интерполяции в новой точке (1 - да, 2 - нет): ')
    return continue_add_points


def read_point(a, b):
    while True:
        try:
            new_x = float(input('Введите значение х для функции интерполяции: '))
            if a <= new_x <= b:
                return new_x
            print('Значение х не входит в диапозон от ' + str(a) + ' до ' + str(b))
        except ValueError:
            print('Неверный формат для х')
