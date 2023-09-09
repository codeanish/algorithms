from src import quick_sort


def test_quick_sort_my_solution():
    assert quick_sort.quick_sort_my_solution([1, 7, 4, 1, 10, 9, 5]) == [1, 1, 4, 5, 7, 9, 10]

def test_quick_sort():
    assert quick_sort.quick_sort([1, 7, 4, 1, 10, 9, 5]) == [1, 1, 4, 5, 7, 9, 10]