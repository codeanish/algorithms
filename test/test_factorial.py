from src import factorial


def test_factorial_recursive():
    assert factorial.factorial_recursive(0) == 0
    assert factorial.factorial_recursive(1) == 1
    assert factorial.factorial_recursive(2) == 2
    assert factorial.factorial_recursive(3) == 6
    assert factorial.factorial_recursive(4) == 24
    assert factorial.factorial_recursive(5) == 120

def test_factorial_iterative():
    assert factorial.factorial_iterative(0) == 0
    assert factorial.factorial_iterative(1) == 1
    assert factorial.factorial_iterative(2) == 2
    assert factorial.factorial_iterative(3) == 6
    assert factorial.factorial_iterative(4) == 24
    assert factorial.factorial_iterative(5) == 120