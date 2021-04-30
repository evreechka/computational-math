from math import sin, cos


def integrate_rectangle(step_num, type_rectangle, a, b, f):
    global checkSecond
    global delta
    step = abs(b - a) / step_num
    correct_interval = True
    if a == b:
        return 0
    if a > b:
        tmp = a
        a = b
        b = tmp
        correct_interval = False
    integral_sum = 0
    x = a
    while x <= b:
        if type_rectangle == 'left':
            integral_sum += f(x) * step
            if checkSecond:
                return 0
        if type_rectangle == 'middle':
            if x != b:
                integral_sum += f(x + step / 2) * step
        if type_rectangle == 'right':
            if x != b:
                integral_sum += f(x + step) * step
        x += step
    if correct_interval:
        return integral_sum
    return -integral_sum


def rule_runge(step_num, accuracy, type_rectangle, a, b, f):
    global checkSecond
    global delta
    I_0 = integrate_rectangle(step_num, type_rectangle, a, b, f)
    if checkSecond:
        return 0
    step_num *= 2
    I_1 = integrate_rectangle(step_num, type_rectangle, a, b, f)
    if checkSecond:
        return 0
    delta = abs(I_1 - I_0) / 3
    while delta > accuracy:
        I_0 = I_1
        step_num *= 2
        I_1 = integrate_rectangle(step_num, type_rectangle, a, b, f)
        if checkSecond:
            return 0
        delta = abs(I_1 - I_0) / 3
    print('\nТочность: ' + str(delta))
    return step_num


def f3(x):
    global delta
    global checkFirst
    if x != 0:
        checkFirst = True
        return sin(x) / x
    checkFirst = True
    return (sin(x + delta)/(x + delta) + (sin(x - delta)/(x - delta))) / 2


def f2(x):
    return x ** 3 - 5 * x ** 2 + 10


def f1(x):
    global checkSecond
    if x == 0:
        checkSecond = True
        return 0
    return 1 / x


def main():
    global checkFirst
    global checkSecond
    global delta
    delta = 0.1
    checkFirst = False
    checkSecond = False
    eval = int(input('Выберете номер уравнения, которое вы хотите проинтегрировать:'
                     '\n1. 1/x'
                     '\n2. x^3 - 5 * x^2 + 10'
                     '\n3. sin(x)/x\n'))
    while eval > 3 or eval < 1:
        eval = int(input('Выберете номер уравнения, которые вы хотите проинтегрировать:'
                         '\n1. 1/x'
                         '\n2. x^3 - 5 * x^2 + 10'
                         '\n3. sin(x)/x\n'))
    a = float(input('Ввведите левую границу промежутка:\na = '))
    print()
    b = float(input('Ввведите правую границу промежутка:\nb = '))
    print()
    accuracy = float(input('Ввведите погрешность:\naccuracy = '))
    if eval == 1:
        curr_fun = f1
        if a * b < 0:
            print('\nВычисление интеграла невозможно, отрезок содержит точку разрыва второго рода')
    elif eval == 2:
        curr_fun = f2
    else:
        curr_fun = f3
    n = rule_runge(5, accuracy, 'left', a, b, curr_fun)
    if not checkSecond:
        result = integrate_rectangle(n, 'left', a, b, curr_fun)
        print('Метод левых прямоугольников: ' + str(result))
        print('Число разбиений: ' + str(n))
        n = rule_runge(5, accuracy, 'right', a, b, curr_fun)
        result = integrate_rectangle(n, 'right', a, b, curr_fun)
        print('Метод правых прямоугольников: ' + str(result))
        print('Число разбиений: ' + str(n))
        n = rule_runge(5, accuracy, 'middle', a, b, curr_fun)
        result = integrate_rectangle(n, 'middle', a, b, curr_fun)
        print('Метод средних прямоугольников: ' + str(result))
        print('Число разбиений: ' + str(n))
        if checkFirst:
            print('\nДанный промежуток содержит точку разрыва первого рода, значение в этой точке заменено на ' + str((sin(delta)/delta + sin(-delta)/(-delta))/2))
    else:
        print('\nВычисление интеграла невозможно, отрезок содержит точку разрыва второго рода')


if __name__ == '__main__':
    main()
