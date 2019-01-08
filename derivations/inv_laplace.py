"""
Generating plots for the inverse Laplace transform to try
to derive it ourselves. Didn't really work out according
to plan, lol.
"""

import matplotlib.pyplot as plt
import numpy as np

from diffeq.laplace import laplace_matrix


def main():
    xs = np.arange(0, 10, 1/100, dtype=np.float64)
    matrix = laplace_matrix(xs, xs)
    inv = np.linalg.inv(matrix)
    plt.plot(xs, inv[1])
    plt.plot(xs, inv[10])
    plt.plot(xs, inv[100])
    plt.plot(xs, inv[500])
    plt.show()


if __name__ == '__main__':
    main()
