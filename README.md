# algorithms
A collection of algorithms I've used to solve problems

## Searches
* [Binary Search](#binary-search) | [My Solution](/src/binary_search.py)

## Sort
* [Quick Sort](#quick-sort) | [My Solution](/src/quick_sort.py)

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

### Quick Sort
Quick sort is a divide and conquer style sorting algorithm. It takes a pivot point in the array, and compares values above and below the pivot point. It then recursively applies the same procedure to the arrays above and below the pivot point until it's left with a single value that doesn't require sorting. It then bubbles all the arrays up and returns a sorted array. In the best and average case scenarios this functions in `O(nlogn)` time, however in the worst case scenario (already sorted), it returns in `O(n^2)` time.

The time taken by this algorithm depends largely on the selection of the pivot point, in an ideal case, you want a value that would correspond to the median of the solution. In the worst case scenario, all numbers in the array are lower than the pivot point or all numbers in the array are higher than the pivot point.

**Procedure**
0. If the length of the array is <= 1, return the array
1. Get pivot point in array rightmost element
2. Loop over all values in the array, if they're less than or equal to the pivot point, put them in a left array, otherwise put them in a right array
3. Return a recursive call to QuickSort(left_array) + Pivot Value + QuickSort(right_array)