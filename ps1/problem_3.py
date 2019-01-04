"""
Solving various parts of problem 3 on the first homework.
"""


INTEREST = 0.05
YEARLY = 12000


def main():
    part_c()
    part_d()


def part_c():
    min_delta = 1000000000
    best_i = 0
    for i in range(0, 300000, 1000):
        delta = abs(i - run_through(i))
        if delta < min_delta:
            min_delta = delta
            best_i = i
    print(best_i)


def part_d():
    min_delta = 1000000000
    best_i = 0
    for i in range(0, 500000, 1000):
        delta = abs(run_through(i))
        if delta < min_delta:
            min_delta = delta
            best_i = i
    print(best_i)


def rate(balance):
    return INTEREST * balance - YEARLY


def run_through(init_balance, num_years=20.0, step=0.01):
    t = 0.0
    balance = init_balance
    while t < num_years:
        balance += rate(balance) * step
        t += step
    return balance


if __name__ == '__main__':
    main()
