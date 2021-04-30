import spline_interpolation
from console_utils import *
from eiler import *


def main():
    cur_functionXY, cur_functionX, x0, y0 = read_function()
    end, eps = read_initial_conditions(x0)
    x, y = method_eiler(x0, y0, end, eps, cur_functionXY, cur_functionX)
    a, b, c, d = spline_interpolation.get_koeff(x, y)
    spline_interpolation.show_graphics(a, b, c, d, x, y, cur_functionX)


if __name__ == '__main__':
    main()
