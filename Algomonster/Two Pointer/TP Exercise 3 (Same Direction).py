# LeetCode 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(self, nums: List[int]) -> None:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    pass

"""
Notes
- TP/SameDirection/Overwrite
- Invariant: finished region is correct

I made mistakes on when I should increment pointers.
It will help thinking what slow, fast represent
This case,
- slow = the "next" position to place a non-zero
- fast = the "next" position to check if it is a non-zero
"""