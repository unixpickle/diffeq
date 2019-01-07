import math

import diffeq.complex as C


def main():
    part_i()
    part_ii()
    part_iii()
    part_iv()
    part_v()


def part_i():
    make_table_entry(complex(1, -1))


def part_ii():
    make_table_entry(C.from_polar(math.pi/6, 2))


def part_iii():
    make_table_entry(next(x for x in C.roots(1j, 2) if x.imag < 0))


def part_iv():
    make_table_entry(next(x for x in C.roots(complex(1), 6)
                          if C.phase(x) < math.pi / 2 and C.phase(x) > 0))


def part_v():
    number = complex(1, 1) / math.sqrt(2)
    angle = -C.phase(number) * 13
    make_table_entry(C.from_polar(angle, 1))


def make_table_entry(number):
    print('%s, sqrt(%f) * exp(i*pi*%f)' % (number, C.mag(number) ** 2, C.phase(number) / math.pi))


if __name__ == '__main__':
    main()
