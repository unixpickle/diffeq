import math


def phase(number):
    res = math.atan2(number.imag, number.real)
    if res < 0:
        res += math.pi * 2
    return res


def mag(number):
    return math.sqrt(number.imag ** 2 + number.real ** 2)


def from_polar(theta, scale):
    return scale * complex(math.cos(theta), math.sin(theta))


def roots(number, n):
    angle = phase(number) / n
    scale = mag(number)
    for i in range(0, n):
        yield from_polar(angle, scale)
        angle += math.pi * 2 / n
