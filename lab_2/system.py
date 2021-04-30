import matplotlib.pyplot as plt
from numpy import arange, meshgrid, linspace
import functions as fun

matrix_jacoby = list()


def determinant_A1(num_system, x1, x2):
    if num_system == '1':
        function1 = fun.f1_1
        diff1 = fun.diff_f1_1_y
        function2 = fun.f2_1
        diff2 = fun.diff_f2_1_y
    else:
        function1 = fun.f1_2
        diff1 = fun.diff_f1_2_y
        function2 = fun.f2_2
        diff2 = fun.diff_f2_2_y
    return function1(x1, x2) * diff2(x1, x2) - function2(x1, x2) * diff1(x1, x2)


def determinant_A2(num_system, x1, x2):
    if num_system == '1':
        function1 = fun.f1_1
        diff1 = fun.diff_f1_1_x
        function2 = fun.f2_1
        diff2 = fun.diff_f2_1_x
    else:
        function1 = fun.f1_2
        diff1 = fun.diff_f1_2_x
        function2 = fun.f2_2
        diff2 = fun.diff_f2_2_x
    return function2(x1, x2) * diff1(x1, x2) - function1(x1, x2) * diff2(x1, x2)


def determinant_jacoby(x1, x2):
    return matrix_jacoby[0](x1, x2) * matrix_jacoby[3](x1, x2) - matrix_jacoby[1](x1, x2) * matrix_jacoby[2](x1, x2)


def checkEnd(x1, x2, new_x1, new_x2, eps):
    if abs(new_x1 - x1) > abs(new_x2 - x2):
        if abs(new_x1 - x1) <= eps:
            return True
    else:
        if abs(new_x2 - x2) <= eps:
            return True
    return False


def method_nyuton(x1, x2, eps, num_system):
    if determinant_jacoby(x1, x2) == 0:
        return []
    new_x1 = x1 - determinant_A1(num_system, x1, x2) / determinant_jacoby(x1, x2)
    new_x2 = x2 - determinant_A2(num_system, x1, x2) / determinant_jacoby(x1, x2)
    iterations = 1
    while not checkEnd(x1, x2, new_x1, new_x2, eps):
        if determinant_jacoby(x1, x2) == 0:
            return []
        x1 = new_x1
        x2 = new_x2
        new_x1 = x1 - determinant_A1(num_system, x1, x2) / determinant_jacoby(x1, x2)
        new_x2 = x2 - determinant_A2(num_system, x1, x2) / determinant_jacoby(x1, x2)
        iterations += 1
    print('Количество итераций: ' + str(iterations))
    return [new_x1, new_x2]


def graph_system(num_system):
    if num_system == '1':
        function1 = fun.graph_f1_1
        function2 = fun.graph_f2_1
    else:
        function1 = fun.graph_f1_2
        function2 = fun.graph_f2_2
    xrange = linspace(-2, 2)
    plt.plot(xrange, function1(xrange))
    plt.plot(xrange, function2(xrange))
    plt.show()


def graph_res_sys(num_system, x, y):
    if num_system == '1':
        function1 = fun.graph_f1_1
        function2 = fun.graph_f2_1
    else:
        function1 = fun.graph_f1_2
        function2 = fun.graph_f2_2
    xrange = linspace(-2, 2)
    plt.plot(xrange, function1(xrange))
    plt.plot(xrange, function2(xrange))
    plt.scatter(x, y, c='b')
    plt.show()


def get_res_sys(num_system):
    graph_system(num_system)
    x = float(input('Введите приближенное значение для x: '))
    y = float(input('Введите приближенное значение для y: '))
    eps = float(input('Введите приближение: '))
    result = method_nyuton(x, y, eps, num_system)
    if not result:
        print("Система не имеет корней")
    else:
        print('x=' + str(result[0]))
        print('y=' + str(result[1]))
        graph_res_sys(num_system, result[0], result[1])
