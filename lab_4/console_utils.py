from math import sin, cos


def f1(x_values):
    y_values = []
    for x in x_values:
        y_values.append(sin(x))
    return y_values


def f2(x_values):
    y_values = []
    for x in x_values:
        y_values.append(cos(x) + sin(x))
    return y_values


def read_function():
    fun_num = 0
    while fun_num == 0:
        try:
            fun_num = int(input('Выберете номер уравнение:'
                                '\n 1. f(x) = sin(x)'
                                '\n 2. f(x) = cos(x) + sin(x)\n'))
            if fun_num < 1 or fun_num > 2:
                print('Неверный номер уравнения :(')
                fun_num = 0
            else:
                if fun_num == 1:
                    return f1
                else:
                    return f2
        except ValueError:
            print('Некорректный номер функции')
            fun_num = 0


def read_interval():
    while True:
        print('Введите левую границу промежутка:')
        try:
            x0 = float(input('x0 = '))
            break
        except ValueError:
            print('Неверный формат x0')
    while True:
        print('Введите правую границу промежутка:')
        try:
            xn = float(input('xn = '))
            break
        except ValueError:
            print('Неверный формат xn')
    if x0 == xn:
        print('Промежуток не может быть пустым!')
        x0, xn = read_interval()
    if x0 > xn:
        return xn, x0
    return x0, xn


def read_nodes_count():
    while True:
        try:
            nodes = int(input('Введите количество узлов: '))
            return nodes
        except ValueError:
            print('Неверный формат количества узлов интерполяции')


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

