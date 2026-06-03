# AlgoMonster Unique Q. Find Element in Sorted Array with Duplicates

""" Question
Given a sorted array of integers and a target integer, 
find the first occurrence of the target and return its index. 
Return -1 if the target is not in the array.

Input:
arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3

Output: 1

Why: The first occurrence of 3 is at index 1.
"""

def find_first_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            right = mid - 1
            res = mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return res

""" 
Notes

You have to seperate equality condition and inequality conditions
You can simply remove right when equality is satisfied
I added this bit instead of removing its right:
if arr[res] != target:
        return -1
"""