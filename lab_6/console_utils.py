def f1_XY(x, y):
    return x ** 2 * y ** 2


def f2_XY(x, y):
    return x ** 2 + y ** 2 + 5


def read_function():
    fun_num = 0
    while fun_num == 0:
        try:
            fun_num = int(input('Выберете номер уравнение:'
                                '\n 1. f(x,y) = x^2 * y^2'
                                '\n 2. f(x,y) = x^2 + y^2 + 5\n'))
            if fun_num < 1 or fun_num > 2:
                print('Неверный номер уравнения :(')
                fun_num = 0
            else:
                if fun_num == 1:
                    return f1_XY
                else:
                    return f2_XY
        except ValueError:
            print('Некорректный номер функции')
            fun_num = 0


def read_interval_x():
    while True:
        print('Введите левую границу промежутка для Х:')
        try:
            x0 = float(input('a = '))
            break
        except ValueError:
            print('Неверный формат a')
    while True:
        print('Введите правую границу промежутка для Х:')
        try:
            xn = float(input('b = '))
            break
        except ValueError:
            print('Неверный формат b')
    if x0 == xn:
        print('Промежуток не может быть пустым!')
        x0, xn = read_interval_x()
    if x0 > xn:
        return xn, x0
    return x0, xn


def read_interval_y():
    while True:
        print('Введите левую границу промежутка для Y:')
        try:
            y0 = float(input('c = '))
            break
        except ValueError:
            print('Неверный формат c')
    while True:
        print('Введите правую границу промежутка для Y:')
        try:
            yn = float(input('d = '))
            break
        except ValueError:
            print('Неверный формат d')
    if y0 == yn:
        print('Промежуток не может быть пустым!')
        y0, yn = read_interval_y()
    if y0 > yn:
        return yn, y0
    return y0, yn


def read_accuracy():
    while True:
        try:
            eps = float(input('Введите погрешность:\neps = '))
            return eps
        except ValueError:
            print('Неверный формат для погрешности!')
