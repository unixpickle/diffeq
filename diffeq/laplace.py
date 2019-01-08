import numpy as np


def laplace_matrix(t_values, s_values):
    """
    Generate a matrix which performs the laplace transform
    when multiplied on the left of a column vector.

    Args:
        t_values: the stops for t.
        s_values: the stops for outputs, s.
    """
    mat = t_values[None] * s_values[:, None]
    res = np.exp(-mat)
    for i in range(len(t_values) - 1):
        res[:, i] *= t_values[i + 1] - t_values[i]
    # We don't technically have a delta_t, so we use
    # the previous one.
    res[:, len(t_values) - 1] *= t_values[-1] - t_values[-2]
    return res
