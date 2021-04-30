import numpy as np
import console_utils
import spline_interpolation


def main():
    cur_function = console_utils.read_function()
    x0, xn = console_utils.read_interval()
    nodes = console_utils.read_nodes_count()
    x = np.linspace(x0, xn, nodes)
    y = cur_function(x)
    a, b, c, d = spline_interpolation.get_koeff(x, y)
    spline_interpolation.show_graphics(a, b, c, d, x, y, cur_function)


if __name__ == '__main__':
    main()
