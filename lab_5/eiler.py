def get_step(x0, y0, eps, fXY, fX):
    step = 10
    while abs(calculate_y(step, y0, x0, fXY) - fX(x0 + step)) > eps:
        step /= 2
    print('Step: ' + str(step))
    return step


def calculate_y(step, prev_y, prev_x, fXY):
    return prev_y + step * fXY(prev_x, prev_y)


def method_eiler(x0, y0, end, eps, fXY, fX):
    step = get_step(x0, y0, eps, fXY, fX)
    x_values = [x0]
    y_values = [y0]
    last_x = x_values[-1]
    while last_x < end:
        x_values.append(last_x + step)
        y_values.append(calculate_y(step, y_values[-1], last_x, fXY))
        last_x = x_values[-1]
    x_values.pop()
    y_values.pop()
    x_values.append(end)
    y_values.append(calculate_y(step, y_values[-1], x_values[-2], fXY))
    return x_values, y_values
