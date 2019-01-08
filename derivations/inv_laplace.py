"""
Generating plots for the inverse Laplace transform to try
to derive it ourselves. Didn't really work out according
to plan, lol.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    matrix = np.zeros((1000, 1000), dtype=np.float64)
    for i in range(1000):
        for j in range(1000):
            matrix[i, j] = np.exp(-i / 100 * j / 100) / 100.0
    # Example of taking a laplace transform.
    # plt.plot(np.arange(0, 10, 1/100), np.dot(matrix, np.arange(0, 10, 1/100)))
    inv = np.linalg.inv(matrix)
    xs = np.arange(0, 10, 1/100, dtype=np.float64)
    plt.plot(xs, inv[1])
    plt.plot(xs, inv[10])
    plt.plot(xs, inv[100])
    plt.plot(xs, inv[500])
    plt.show()


if __name__ == '__main__':
    main()
