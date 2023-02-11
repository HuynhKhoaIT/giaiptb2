import math

def solve_quadratic_equation(a, b, c):
    if a == 0:
        return None

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2

print(solve_quadratic_equation(1, -3, 2))