import math


def f(z):
    sum1 = 0
    for i in range(1, len(z) + 1):
        sum1 += 78 * pow(z[math.ceil(i/4) - 1], 2) + \
            pow(z[math.ceil(i/4) - 1], 3) + 3
    return sum1 * 39


def main(z):
    return f(z)

assert (main([0.02, 0.56, 0.45, 0.95, -0.06, -0.85])) == 2.63e+03
print(main([-0.53, 0.47, -0.19, 0.9, 0.11, -0.88]))