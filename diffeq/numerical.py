"""
Numerical methods for solving diff eqs.
"""


def euler_step(f, x0, y0, h):
    """
    Perform a step of Euler's method.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    slope = f(x0, y0)
    return x0 + h, y0 + h * slope


def rk2_step(f, x0, y0, h):
    """
    Perform a step of rk2.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    slope1 = f(x0, y0)
    slope2 = f(x0 + h, y0 + h * slope1)
    slope = (slope1 + slope2) / 2
    return x0 + h, y0 + h * slope


def rk3_step(f, x0, y0, h):
    """
    Perform a step of RK3.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    # https://people.revoledu.com/kardi/tutorial/ODE/Runge%20Kutta%203.htm
    k1 = f(x0, y0)
    k2 = f(x0 + 0.5 * h, y0 + 0.5 * h * k1)
    k3 = f(x0 + h, y0 - k1 * h + 2 * k2 * h)
    return x0 + h, y0 + h * (k1 + 4 * k2 + k3) / 6.0


def third_order_step(f, x0, y0, h):
    """
    Perform a step of a third-order method I invented.

    See derivations/third_order.jpg.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    a = 1.0 / 4.0
    b = 3.0 / 4.0
    c = 2.0 / 3.0
    # Get the exact initial slope.
    slope1 = f(x0, y0)
    # Use RK2 to get f(ch) + O(h^3)
    slope2 = f(x0 + c * h, y0 + c * h * slope1)
    slope3 = (slope1 + slope2) / 2
    # Get the slope at (ch, f(ch) + O(h^3)),
    # which is f'(ch) + O(h^3).
    slope4 = f(x0 + c * h, y0 + c * h * slope3)
    # Compute f(h) + O(h^4).
    return x0 + h, y0 + h * (a * slope1 + b * slope4)


def fourth_order_step(f, x0, y0, h):
    """
    Perform a step of a fourth-order method I invented.

    See derivations/fourth_order_*.jpg.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    third_a = 1.0 / 4.0
    third_b = 3.0 / 4.0
    third_c = 2.0 / 3.0

    fourth_a = 1.0 / 10.0
    fourth_b = 2.0 / 5.0
    fourth_c = 1.0 / 2.0
    fourth_d = 1.0 / 3.0
    fourth_e = 5.0 / 6.0

    # Get information needed for RK2.
    slope1 = f(x0, y0)
    # slope2 = f(x0 + h, y0 + h * slope1)

    def second_order(step):
        slope2 = f(x0 + h * step, y0 + h * slope1 * step)
        slope = (slope1 + slope2) / 2
        return f(x0 + h * step, y0 + h * step * slope)
        # Old method
        # b = (step ** 2) / 2.0
        # a = step - b
        # slope = a * slope1 + b * slope2
        # return f(x0 + h * step, y0 + h * step * slope)

    def third_order(step):
        sub_step = third_c * step
        tmp_slope = second_order(sub_step)
        return f(x0 + h * step, y0 + h * step * (third_a * slope1 + third_b * tmp_slope))

    df_eh = third_order(fourth_e)
    df_dh = third_order(fourth_d)

    return x0 + h, y0 + h * (fourth_a * slope1 + fourth_b * df_eh + fourth_c * df_dh)


def numerical_solve(f, x0, y0, x1, h=0.01, step_fn=rk3_step):
    """
    Numerically solve a differential equation.

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        x1: the x to run until.
        h: the step size.
        step_fn: a function to take one step of the
          algorithm.

    Returns:
        An iterator of (x, y) tuples along the curve.
    """
    x = x0
    y = y0
    yield (x, y)
    while x < x1:
        x, y = step_fn(f, x, y, h)
        yield (x, y)
