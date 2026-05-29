# AlgoMonster Q. First Element Not Smaller Than Target 
# No LeetCode Q that is same as this one

""" Question
Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

Input:
arr = [1, 3, 3, 5, 8, 8, 10]
target = 2

Output: 1
"""

def first_not_smaller(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

""" 
Explanation

Becareful about what side I need to remove if feasible is True
"""