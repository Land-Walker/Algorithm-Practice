# LeetCode 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

def peakIndexInMountainArray(self, arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

""" 
Notes

yeap, I got confused with this one to Exercise 4.
Got correct in one try.
"""