"""
Empirically evaluate the asymptotic error behavior of
different numerical methods of solving diff eqs.
"""

import math

import numpy as np
from scipy.integrate import odeint

from diffeq.numerical import (euler_step, rk2_step, rk3_step, third_order_step, fourth_order_step,
                              numerical_solve)


STEP_FNS = {
    'euler': euler_step,
    'rk2': rk2_step,
    'rk3': rk3_step,
    '3rd': third_order_step,
    '4th': fourth_order_step,
}


def main():
    print('Evaluating single steps...')
    evaluate_steps()
    print('Evaluating full solutions...')
    evaluate_solutions()
    print('Evaluating 3D rk2...')
    evaluate_3d_rk2()


def evaluate_steps():
    fns = [lambda x, y: y ** 2 - x,
           lambda x, y: x ** 2 - y,
           lambda x, y: math.sin(x) * math.cos(y)]
    for i, fn in enumerate(fns):
        print('Equation %d:' % i)
        solution1 = odeint(fn, 0, [1, 1.15], tfirst=True)[-1][0]
        solution2 = odeint(fn, 0, [1, 1.3], tfirst=True)[-1][0]
        for name, step_fn in STEP_FNS.items():
            _, approx1 = step_fn(fn, 1, 0, 0.15)
            _, approx2 = step_fn(fn, 1, 0, 0.3)
            error1 = abs(approx1 - solution1)
            error2 = abs(approx2 - solution2)
            print(' - %s: halving factor %f (error=%e)' % (name, error2 / error1, error1))


def evaluate_solutions():
    fns = [lambda x, y: y ** 2 - x,
           lambda x, y: x ** 2 - y,
           lambda x, y: math.sin(x) * math.cos(y)]
    for i, fn in enumerate(fns):
        print('Equation %d:' % i)
        solution = odeint(fn, 0, [1, 2], tfirst=True)[-1][0]
        for name, step_fn in STEP_FNS.items():
            solution1 = last(numerical_solve(fn, 1, 0, 2, h=0.1, step_fn=step_fn))[1]
            solution2 = last(numerical_solve(fn, 1, 0, 2, h=0.05, step_fn=step_fn))[1]
            error1 = abs(solution - solution1)
            error2 = abs(solution - solution2)
            print(' - %s: halving factor %f (error=%e)' % (name, error1 / error2, error2))


def evaluate_3d_rk2():
    def fn(var, t):
        x, y, z = var[0], var[1], var[2]
        return np.array([x**2 - z, y**2 + x - z**2 + 1, y + x ** 2])

    def mv_rk2(step_size):
        x = np.array([0, 0, 0], dtype=np.float64)
        for i in range(round(1 / step_size)):
            t = i * step_size
            dx = fn(x, t)
            dx1 = fn(x + step_size * dx, t + step_size)
            x = x + step_size * (dx + dx1) / 2
        return x

    soln = odeint(fn, [0, 0, 0], [0.0, 1.0])[-1]
    error1 = np.sum(np.abs(mv_rk2(0.01) - soln))
    error2 = np.sum(np.abs(mv_rk2(0.005) - soln))
    print(' - Halving factor: %f' % (error1 / error2))


def last(iterator):
    y = None
    for x in iterator:
        y = x
    return y


if __name__ == '__main__':
    main()
