# LeetCode 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    res = -1
    if len(nums) == 1:
        return nums[0]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= nums[-1]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return nums[res]

""" 
Notes

Initial code used < arr[right] as a feasible function
This got two problems:
1. right is moving, while my idea is to compare with the rightmost element
2. < cannot handle cases where the answer is the rightmost element

Therefore, it must be <= arr[-1]
"""