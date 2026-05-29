# LeetCode 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

def square_root(n: int) -> int:
    left, right = 0, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid**2 <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

""" 
Explanation

Realize that mid**2 <= n is the feasible function.
I chose less than since we truncate the decimals, so we need to remove the smaller parts.
"""