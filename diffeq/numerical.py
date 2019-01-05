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

    Args:
        f: the slope as a function of x, y.
        x0: the start x.
        y0: the start y.
        h: the step size.

    Returns:
        A tuple (x1, y1).
    """
    slope1 = f(x0, y0)
    slope2 = f(x0 + 1.0 / 3.0 * h, y0 + 1.0 / 3.0 * h * slope1)
    slope3 = (slope1 + slope2) / 2
    slope4 = f(x0 + 1.0 / 3.0 * h, y0 + 1.0 / 3.0 * h * slope3)
    return x0 + h, y0 + h * (-0.5 * slope1 + 3.0 / 2.0 * slope4)


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
