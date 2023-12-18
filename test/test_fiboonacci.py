from src import fibonacci

def test_fibonacci_recursive():
    assert fibonacci.fibonacci(0) == 0
    assert fibonacci.fibonacci(1) == 1
    assert fibonacci.fibonacci(2) == 1
    assert fibonacci.fibonacci(3) == 2
    assert fibonacci.fibonacci(4) == 3
    assert fibonacci.fibonacci(5) == 5
    assert fibonacci.fibonacci(6) == 8
    assert fibonacci.fibonacci(7) == 13
    assert fibonacci.fibonacci(8) == 21
    assert fibonacci.fibonacci(9) == 34
    assert fibonacci.fibonacci(30) == 514229