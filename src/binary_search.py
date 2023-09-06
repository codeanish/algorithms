from typing import List
import math

def binary_search_blind_implementation(search_array: List[int], search_value: int) -> int:

    # For small arrays, don't do binary search
    if search_array[0] == search_value:
        return 0
    if len(search_array) == 2:
        # Don't need to check for search_array[0] as I did that separately before
        if search_array[1] == search_value:
            return 1
        else:
            return None
    
    left_index = 0
    mid_index = math.ceil(len(search_array)/2) -1
    right_index = len(search_array) - 1
    remaining_elements = len(search_array)

    # Check if search value is out of bounds
    if search_value < search_array[left_index] or search_value > search_array[right_index]:
        return None

    while(remaining_elements > 3):
        left_value = search_array[left_index]
        if left_value == search_value:
            return left_index
        mid_value = search_array[mid_index]
        if mid_value == search_value:
            return mid_index
        right_value = search_array[right_index]
        if right_value == search_value:
            return right_index
        if left_value <= search_value < mid_value:
            right_index = mid_index
            mid_index = math.ceil(right_index/2)
            remaining_elements = right_index - left_index + 1
        if mid_value <= search_value <= right_value:
            left_index = mid_index
            mid_index = left_index + math.ceil((right_index-left_index)/2)
            remaining_elements = right_index - left_index + 1
        
        
    if search_value == search_array[left_index]:
        return left_index
    elif search_value == search_array[mid_index]:
        return mid_index
    elif search_value == search_array[right_index]:
        return right_index
    else:
        return None


def binary_search_proper_implementation(search_array: List[int], search_value) -> int:
    left = 0
    right = len(search_array) - 1
    mid = 0
    while left <= right:
        mid = math.floor((left + right)/2)
        if search_array[mid] < search_value:
            left = mid + 1
        elif search_array[mid] > search_value:
            right = mid - 1
        # Means that the search value is at mid
        else:
            return mid
    return None

if __name__ == "__main__":
    print(binary_search_blind_implementation([2,4,6,8,10],10))