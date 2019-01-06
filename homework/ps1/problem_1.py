"""
Solving various parts of problem 1 on the first homework.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()


def part_a():
    xs = []
    ys = []
    us = []
    vs = []
    for i in range(-20, 20):
        for j in range(-20, 20):
            x = i / 5
            y = j / 5
            xs.append(x)
            ys.append(y)
            vector = np.array([1, slope_fn(x, y)], dtype=np.float)
            vector /= np.linalg.norm(vector)
            us.append(vector[0])
            vs.append(vector[1])
    plt.quiver(xs, ys, us, vs)
    plt.plot(*make_solution(0, 0))
    plt.plot(*make_solution(1, 0))
    plt.plot(*make_solution(0, -2))
    plt.plot(*make_solution(0, 2))
    plt.plot(*make_solution(1, 1))
    plt.show()


def part_b():
    xs = []
    ys = []
    for i in range(-20, 20):
        x = i / 5
        for j in range(100, -100, -1):
            y = j / 20
            if slope_fn(x, y) <= 0:
                xs.append(x)
                ys.append(y)
                break
    plt.plot(xs, ys)
    plt.plot(xs, np.sqrt(xs))
    plt.show()


def part_c():
    x = 1.25
    y = -0.5
    print('slope should be -1:', slope_fn(x, y))


def part_d():
    plt.plot(*make_solution(1.25, -0.5, lim=10))
    plt.plot(*make_solution(1.25, -0.6, lim=10))
    plt.plot(*make_solution(1.25, -1.0, lim=10))
    plt.plot(*make_solution(1.25, -2.0, lim=10))
    xs = np.array([i / 10 for i in range(-100, 100)])
    plt.plot(xs, -np.sqrt(xs))
    plt.show()


def part_e():
    plt.plot(*make_solution(0.8, 1.0, lim=10))
    plt.plot(*make_solution(1.25, -2.0, lim=10))
    xs = np.array([i / 10 for i in range(-100, 100)])
    plt.plot(xs, np.sqrt(xs))
    plt.plot(xs, -np.sqrt(xs))
    plt.show()


def make_solution(start_x, start_y, step_size=0.01, lim=4):
    xs = []
    ys = []
    x = start_x
    y = start_y
    for _ in range(1000):
        y += step_size * slope_fn(x, y)
        x += step_size
        if y > lim or x > lim:
            break
        xs.append(x)
        ys.append(y)
    return xs, ys


def slope_fn(x, y):
    return y ** 2 - x


if __name__ == '__main__':
    main()
