"""
Deriving a fourth-order numerical method.

In particular, this script solves the system of equations
needed to derive the coefficients for the method.

Solution:

    a = 1/10
    b = 2/5
    c = 1/2
    d = 1/3
    e = 5/6

"""


def main():
    for b in iterate_values():
        for c in iterate_values():
            for d in iterate_values():
                e = (c * d - 1 / 2) / -b
                a = 1 - (b + c)
                if satisfied(a, b, c, d, e):
                    print(a, b, c, d, e)
                    return


def iterate_values():
    for num in range(-6, 6):
        if num == 0:
            continue
        for denom in range(1, 6):
            yield num / denom


def satisfied(a, b, c, d, e):
    tol = 1e-4
    if abs(1 - a - b - c) > tol:
        return False
    if abs(1/2 - b * e - c * d) > tol:
        return False
    if abs(1/6 - 1/2 * b * e ** 2 - 1/2 * c * d ** 2) > tol:
        return False
    if abs(1/24 - 1/6 * b * e ** 3 - 1/6 * c * d ** 3) > tol:
        return False
    return True


if __name__ == '__main__':
    main()
