# Binary Search
## What it is
Binary Search = Array Search algorithm
- Works by narrowing the search range by half
- Works in sorted array
- Pick the middle element in the current search range
- Compare options, Discard half of them
- Can be used recursively or iteratively
  - Recursively: O(log(N))
  - Iteratively: O(1)

## Implementation
1. Search Range = between left & right pointers
   - which move towards each other during searching
2. Examine mid index of the range
   - if it is smaller than target, discard everything on left from mid, vice versa
3. Continue step 2 until we find the correct one in sorted array

~~~python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    # <= because left and right could point to the same element, < would miss it
    while left <= right:
        # double slash for integer division in python 3,
        # we don't have to worry about integer `left + right` overflow
        # since python integers can be arbitrarily large
        mid = (left + right) // 2
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1  # if we get here we didn't hit above return so we didn't find target
~~~

## Deducing Binary Search (Core Elements)
1. When to terminate the loop
   - while loop must contain equality (=), otherwise the loop might be skipped and miss potential match (e.g. edge cases like one-element array)
2. How to update left & right boundary in if conditions
   - Consider which side, and if mid < target, discard all left by left = mid + 1
3. Should I discard the current element?
  - Depends, but in vanilla, we can discard

## When to use Binary Search
Beyond sorted array, wherever a binary decision to shrink the search range must be made.