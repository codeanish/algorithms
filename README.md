# algorithms
A collection of algorithms I've used to solve problems

## Searches
* [Binary Search](#binary-search) | [My Solution](/src/binary_search.py)

### Binary Search
Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.  

Binary search runs in logarithmic time in the worst case, making `O(log n)` comparisons, where n is the number of elements in the array. Binary search is faster than linear search except for small arrays. However, the array must be sorted first to be able to apply binary search.

**Procedure**
1. Set left_index = 0 & Set right_index = n - 1
2. If left_index > right_index the search terminates unsuccessfully
3. Set mid_index = floor((right_index-left_index)/2)
4. If search_array[mid_index] < search_value - the search is less than the midpoint, set right_index = mid_index -1
5. If search_array[mid_index] > search_value - the search is more than the midpoint, set left_index = mid_index + 1
6. search_value = search_array[mid_index], return mid_index