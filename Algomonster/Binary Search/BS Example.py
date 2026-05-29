# Find the First True in a Sorted Boolean Array (AlgoMonster Unique Q)

# Question
"""
An array of boolean values is divided into two sections: 
The left section consists of all false, and the right section consists of all true. 
Find the First True in a Sorted Boolean Array of the right section
(i.e. the index of the first true element)
If there is no true element, return -1.

Input: arr = [false, false, true, true, true]

Output: 2

Why: The first true's index is 2.
"""

def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] != True:
            left = mid + 1
        else:
            right = mid - 1
            res = mid
    return res

""" 
Explanation

Binary search, store the mid just in case.
Remove right when feasible func is True
Remove left when feasible func is False
"""