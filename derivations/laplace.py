"""
Plotting the laplace transforms of various functions.
"""

import matplotlib.pyplot as plt
import numpy as np

from diffeq.laplace import laplace_matrix


def main():
    ts = np.arange(0, 100, 1/100, dtype=np.float64)
    ss = np.arange(1.5, 10, 1/100, dtype=np.float64)
    matrix = laplace_matrix(ts, ss)
    plt.plot(ss, np.dot(matrix, ts))
    plt.plot(ss, np.dot(matrix, np.square(ts)))
    plt.plot(ss, np.dot(matrix, np.exp(ts)))
    plt.plot(ss, np.dot(matrix, np.cos(ts)))
    plt.plot(ss, np.dot(matrix, [1] * 10000))
    plt.legend(['L{t}', 'L{t^2}', 'L{e^t}', 'L{cos(t)}', 'L{1}'])
    plt.show()


if __name__ == '__main__':
    main()
