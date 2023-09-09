from typing import List


def quick_sort_my_solution(nums: List[int]) -> List[int]:
    right_index = len(nums) - 1
    pivot_value = nums[right_index]
    left_nums = []
    right_nums = []
    for num in nums[0:right_index]:
        if num <= pivot_value:
            left_nums.append(num)
        else:
            right_nums.append(num)
    left_elements = len(left_nums)
    right_elements = len(right_nums)
    if left_elements > 1:
        left_nums = quick_sort_my_solution(left_nums)
    if right_elements > 1:
        right_nums = quick_sort_my_solution(right_nums)
    left_nums.append(pivot_value)
    left_nums.extend(right_nums)
    return left_nums


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    # Takes the last value from the array and removes it from the array
    pivot_value = nums.pop()
    left_elements = []
    right_elements = []
    for num in nums:
        if num <= pivot_value:
            left_elements.append(num)
        else:
            right_elements.append(num)
    return quick_sort(left_elements) + [pivot_value] + quick_sort(right_elements)

if __name__ == "__main__":
    test_nums = [1, 7, 4, 1, 10, 9, 5]
    print(quick_sort_my_solution(test_nums))
    print(quick_sort(test_nums))
