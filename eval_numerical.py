"""
Empirically evaluate the asymptotic error behavior of
different numerical methods of solving diff eqs.
"""

import math

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


def last(iterator):
    y = None
    for x in iterator:
        y = x
    return y


if __name__ == '__main__':
    main()
