import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

cache: dict[int,int] = {}

def fibonacci_memoized(n: int) -> int:
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    return cache[n]


if __name__ == "__main__":
    fib_to_find = 30

    start = time.perf_counter()
    fib = fibonacci(fib_to_find)
    end = time.perf_counter()
    print(f"Fib = {fib} in {end - start:0.4f} seconds")

    start = time.perf_counter()
    fib_memoized = fibonacci_memoized(fib_to_find)
    end = time.perf_counter()
    print(f"Fib = {fib_memoized} in {end - start:0.4f} seconds")