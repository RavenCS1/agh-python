import time
import math

import functions
from vector import Vector2D as CVector2D


def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def scale(self, factor):
        self.x *= factor
        self.y *= factor

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def add(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError
        self.x += other.x
        self.y += other.y






print("\n==== sum_of_squares ====")

N = 10**6

start = time.time()
print("C:", functions.sum_of_squares(N))
print("C time:", time.time() - start)

start = time.time()
print("Python:", sum_of_squares(N))
print("Python time:", time.time() - start)



print("\n==== fibonacci ====")

FIB_N = 30

start = time.time()
print("C:", functions.fibonacci(FIB_N))
print("C time:", time.time() - start)

start = time.time()
print("Python:", fibonacci(FIB_N))
print("Python time:", time.time() - start)


print("\n==== Vector2D Benchmark ====")

VECTOR_N = 100000

def vector_test(cls, label):
    
    v = cls(1.0, 2.0)

    start = time.time()
    
    for _ in range(VECTOR_N):
        v.scale(1.001)
        
    scale_time = time.time() - start


    start = time.time()
    
    m = 0.0
    for _ in range(VECTOR_N):
        m += v.magnitude()
        
    magnitude_time = time.time() - start


    v2 = cls(0.1, 0.2)
    
    start = time.time()
    
    for _ in range(VECTOR_N):
        v.add(v2)
        
    add_time = time.time() - start

    print(f"\n{label} Vector2D:")
    print(f"  scale():     {scale_time:.6f}s")
    print(f"  magnitude(): {magnitude_time:.6f}s")
    print(f"  add():       {add_time:.6f}s")
    print(f"  Final: {v} | Magnitude: {v.magnitude():.4f}")


vector_test(CVector2D, "C")
vector_test(Vector2D, "Python")