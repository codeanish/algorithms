from src import fibonacci

def test_fibonacci_iterative():
    assert fibonacci.fibonacci_sum_iterative(0) == 0
    assert fibonacci.fibonacci_sum_iterative(1) == 1
    assert fibonacci.fibonacci_sum_iterative(2) == 3
    assert fibonacci.fibonacci_sum_iterative(3) == 6
    assert fibonacci.fibonacci_sum_iterative(4) == 10

def test_fibonacci_iterative_while():
    assert fibonacci.fibonacci_sum_iterative_while(0) == 0
    assert fibonacci.fibonacci_sum_iterative_while(1) == 1
    assert fibonacci.fibonacci_sum_iterative_while(2) == 3
    assert fibonacci.fibonacci_sum_iterative_while(3) == 6
    assert fibonacci.fibonacci_sum_iterative_while(4) == 10

def test_fibonacci_recursive():
    assert fibonacci.fibonacci_recursive(0) == 0
    assert fibonacci.fibonacci_recursive(1) == 1
    assert fibonacci.fibonacci_recursive(2) == 3
    assert fibonacci.fibonacci_recursive(3) == 6
    assert fibonacci.fibonacci_recursive(4) == 10