// LeetCode 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/description/

void moveZeroes(vector<int>& nums) {
    int slow = 0;
    for (int fast = 0; fast < nums.size(); fast++) {
        if (nums[fast] != 0) {
            std::swap(nums[slow], nums[fast]);
            slow++;
        }
    }
}

/* Explanation

*/