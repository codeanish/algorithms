def fibonacci_sum_iterative(n: int):
    fib = 0
    for i in range(1,n+1):
        fib += i
    return fib

def fibonacci_sum_iterative_while(n: int):
    fib = 0
    while n >= 0:
        fib += n
        n -= 1
    return fib

def fibonacci_recursive(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + fibonacci_recursive(n-1)