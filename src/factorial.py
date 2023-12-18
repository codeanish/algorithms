def factorial_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n*factorial_recursive(n-1)

def factorial_iterative(n: int):
    if n == 0:
        return 0
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    return factorial


if __name__ == "__main__":
    print(factorial_recursive(10))
