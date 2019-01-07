import math

import matplotlib.pyplot as plt
import numpy as np

from diffeq.numerical import numerical_solve

STARTIUM_HL = 2.0
MEDIUM_HL = 3.0
LOG_2 = math.log(2)


def main():
    part_a()
    part_b()
    part_d()
    part_e()


def part_a():
    ts, xs, ys, zs = list(zip(*run_euler()))
    plt.plot(ts, xs)
    plt.plot(ts, ys)
    plt.plot(ts, zs)
    plt.legend(['x', 'y', 'z'])
    plt.show()


def part_b():
    last_y = None
    for _, y in numerical_solve(dx_dt, 0, 1, STARTIUM_HL, h=STARTIUM_HL / 1000):
        last_y = y
    print('should be 0.5: %f' % last_y)


def part_d():
    max_t = 0
    max_y = 0
    for t, _, y, _ in run_euler():
        if y > max_y:
            max_y = y
            max_t = t
    print('t is %f' % max_t)


def part_e():
    regular = run_euler()
    scaled = run_euler(init_value=2.0)
    ratios = []
    next(regular)
    next(scaled)
    for (_, x1, y1, z1), (_, x2, y2, z2) in zip(regular, scaled):
        ratios.append(x2 / x1)
        ratios.append(y2 / y1)
        ratios.append(z2 / z1)
    print('should be 2: %f' % np.mean(ratios))


def dx_dt(t, x):
    return -LOG_2 / STARTIUM_HL * x


def dy_dt(t, x, y):
    return (LOG_2 / (2 * STARTIUM_HL) * x - LOG_2 / MEDIUM_HL * y)


def dz_dt(t, x, y):
    return (LOG_2 / (2 * STARTIUM_HL) * x + LOG_2 / MEDIUM_HL * y)


def run_euler(init_value=1.0):
    x = init_value
    y = 0
    z = 0
    t = 0.0
    dt = 0.01
    for i in range(1000):
        dx = dt * dx_dt(t, x)
        dy = dt * dy_dt(t, x, y)
        dz = dt * dz_dt(t, x, y)
        yield (t, x, y, z)
        t += dt
        x += dx
        y += dy
        z += dz


if __name__ == '__main__':
    main()
