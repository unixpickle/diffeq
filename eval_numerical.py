import math

from scipy.integrate import odeint

from diffeq.numerical import euler_step, rk2_step, rk3_step, numerical_solve


def main():
    evaluate_steps()


def evaluate_steps():
    fns = [lambda x, y: y ** 2 - x,
           lambda x, y: x ** 2 - y,
           lambda x, y: math.sin(x) * math.cos(y)]
    step_fns = {'euler': euler_step, 'rk2': rk2_step, '3rd': rk3_step}
    for i, fn in enumerate(fns):
        print('Equation %d:' % i)
        solution = odeint(fn, 0, [1, 2], tfirst=True)[-1][0]
        for name, step_fn in step_fns.items():
            solution1 = last(numerical_solve(fn, 1, 0, 2, h=0.02, step_fn=step_fn))[1]
            solution2 = last(numerical_solve(fn, 1, 0, 2, h=0.01, step_fn=step_fn))[1]
            error1 = abs(solution - solution1)
            error2 = abs(solution - solution2)
            print(' - %s: halving factor %f' % (name, error1 / error2))


def last(iterator):
    y = None
    for x in iterator:
        y = x
    return y


if __name__ == '__main__':
    main()
