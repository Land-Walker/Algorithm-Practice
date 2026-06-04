# LeetCode 26. Remove Duplicates from Sorted Array
# http://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(self, nums: List[int]) -> int:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

"""
Notes

Simple.

TP/Same Direction/Overwrite

Invariant: remaining list positions is all the answers
"""