import evalution as eval
import functions as fun
import system as sys


def main():
    exercise = input('Что вы хотите решить:\n1 - система нелинейных уравнений\n2 - нелинейное уравнение\n')
    if exercise == '1':
        curr_system = input('Выберите систему:\n'
                            'x^3 - x^2 + 2 - y = 0\n'
                            'exp(x) - y = 0\n\n'
                            'x^3 - y = 0\n'
                            'sin(x) - cos(x) + 2 - y = 0\n')
        if curr_system == '1':
            sys.matrix_jacoby.append(fun.diff_f1_1_x)
            sys.matrix_jacoby.append(fun.diff_f2_1_x)
            sys.matrix_jacoby.append(fun.diff_f1_1_y)
            sys.matrix_jacoby.append(fun.diff_f2_1_y)
        if curr_system == '2':
            sys.matrix_jacoby.append(fun.diff_f1_2_x)
            sys.matrix_jacoby.append(fun.diff_f2_2_x)
            sys.matrix_jacoby.append(fun.diff_f1_2_y)
            sys.matrix_jacoby.append(fun.diff_f2_2_y)
        sys.get_res_sys(curr_system)
    elif exercise == '2':
        list_koef = list()
        input_way = input(
            'Выберите способ ввода уравнений:\n' + '1 - Ввести коэффицинты вручную\n' + '2 - Выбрать имеющиеся уравнения\n')
        if input_way == '1':
            bitness = int(input('Введите разрядность уравнения: '))
            print(bitness)
            for i in range(0, bitness + 1):
                value = int(input('Введите коэффициент: '))
                list_koef.append(value)
            eval.get_res_eval(fun.new_function, bitness, list_koef)
        elif input_way == '2':
            evaluation = input('Выберите уравнение(введите номер уравнения)\nf1(x): x^2 + 1 = 0\nf2(x): 6x^2 + 2x '
                               '- 4 = 0\nf3(x): x^3 - 9x= 0\n')
            if evaluation == '1':
                bitness = 2
                list_koef.append(1)
                list_koef.append(0)
                list_koef.append(1)
                eval.get_res_eval(fun.new_function, bitness, list_koef)
            elif evaluation == '2':
                bitness = 2
                list_koef.append(6)
                list_koef.append(2)
                list_koef.append(-4)
                eval.get_res_eval(fun.new_function, bitness, list_koef)
            elif evaluation == '3':
                bitness = 3
                list_koef.append(1)
                list_koef.append(0)
                list_koef.append(-9)
                list_koef.append(0)
                eval.get_res_eval(fun.new_function, bitness, list_koef)


if __name__ == '__main__':
    main()
