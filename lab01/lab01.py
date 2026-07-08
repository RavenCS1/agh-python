from math import sqrt
from cmath import sqrt as csqrt

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    print(f"Quadratic equation: {a}x^2 + {b}x + {c}")

    delta = b * b - 4 * a * c

    if delta > 1e-6:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print(f"Roots: {x1:.3f}, {x2:.3f}")
    elif abs(delta) <= 1e-6:
        x = -b / (2 * a)
        print(f"Double root: {x:.3f}")
    else:
        x1 = (-b - csqrt(delta)) / (2 * a)
        x2 = (-b + csqrt(delta)) / (2 * a)
        print(f"Roots: {x1:.3f}, {x2:.3f}")

if __name__ == "__main__":
    main()