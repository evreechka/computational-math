from console_utils import *
from integral_utils import *


def main():
    function = read_function()
    a, b = read_interval_x()
    c, d = read_interval_y()
    eps = read_accuracy()
    step_num = rule_runge(10, eps, a, b, c, d, function, cells_method)
    print('Приблизительное значение вычислиненного интеграла методом ячеек:')
    print('I ≈ ' + str(cells_method(step_num, a, b, c, d, function)))
    step_num = rule_runge(10, eps, a, b, c, d, function, trapeze_method)
    print('Приблизительное значение вычислиненного интеграла методом трапеций:')
    print('I ≈ ' + str(trapeze_method(step_num, a, b, c, d, function)))
    step_num = rule_runge(10, eps, a, b, c, d, function, left_rectangle_method)
    print('Приблизительное значение вычислиненного интеграла методом левых прямоугольников:')
    print('I ≈ ' + str(left_rectangle_method(step_num, a, b, c, d, function)))
    step_num = rule_runge(10, eps, a, b, c, d, function, middle_rectangle_method)
    print('Приблизительное значение вычислиненного интеграла методом средних прямоугольников:')
    print('I ≈ ' + str(middle_rectangle_method(step_num, a, b, c, d, function)))
    step_num = rule_runge(10, eps, a, b, c, d, function, right_rectangle_method)
    print('Приблизительное значение вычислиненного интеграла методом правых прямоугольников:')
    print('I ≈ ' + str(right_rectangle_method(step_num, a, b, c, d, function)))


if __name__ == '__main__':
    main()
