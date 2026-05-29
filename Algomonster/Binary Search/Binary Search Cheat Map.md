# Cheat Map (how to solve Qs easily)
## Monotonic Function
Monotonic Function = a non-increasing/decreasing function
- We can use binary search if the input is monotonic function

Example:
- sorted array
- functions that contain only True and False (FFFFTTTTT)

## Template
~~~python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
~~~

## Template Explanation
All BS Qs can be simplified as finding a monotonic function (a.k.a. feasible function) that retuns True or False. 

If we find feasible function, the Q becomes Find the First True in a Sorted Boolean Array.

Therefore, with the template, all we need to find is feasible.