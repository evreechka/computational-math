from numpy import exp, sin, cos


def graph_f1_1(x):
    return x ** 3 - x ** 2 + 2


def graph_f2_1(x):
    return exp(x)


def graph_f1_2(x):
    return x ** 3


def graph_f2_2(x):
    return (sin(x) + cos(x)) / 2


def f1_1(x, y):
    return x ** 3 - x ** 2 + 2 - y


def f2_1(x, y):
    return exp(x) - y


def f1_2(x, y):
    return x ** 3 - y


def f2_2(x, y):
    return sin(x) + cos(x) - 2 * y


def diff_f1_1_x(x, y):
    return 3 * x ** 2 - 2 * x


def diff_f2_1_x(x, y):
    return exp(x)


def diff_f1_1_y(x, y):
    return -1


def diff_f2_1_y(x, y):
    return -1


def diff_f1_2_x(x, y):
    return 3 * x ** 2 - y


def diff_f2_2_x(x, y):
    return cos(x) - sin(x)


def diff_f1_2_y(x, y):
    return -1


def diff_f2_2_y(x, y):
    return -2


def new_function(x, bitness, list_koef):
    result = 0
    for i in range(0, bitness + 1):
        result += (x ** (bitness - i)) * list_koef[i]
    return result
