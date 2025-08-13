# LC Q.15 3Sum

2025.08.13. / 08.14.

Difficulty: #easy

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:50 (2nd Try)

End Time: 23:37 (1st Try)

## My Approaches

### Basic Ideas
Use two pointers like Q167.

### Submission Code 1 (Failed)
~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int l = 0;
        int r = nums.size() -1;
        int target = 0;

        while (l < r) {
            for (int i{1}; i < r; ++i) {
                cout << l << " " << r << " ";
                if (nums[l] + nums[l + i] + nums[r] == 0) {
                    res.push_back({nums[l], nums[l + i], nums[r]});
                    ++l;
                } else {
                    ++l;
                }
            }
            l = 0;
            --r;
        }

        return res;
    }
};
~~~

The pointers seem working correctly, but cannot detect two or more sets.
WHYYYYYY?????

Some hints from Claude.ai:
1. Missing Critical Step: Three-sum problems typically require the array to be sorted first. Without sorting, you can't effectively use two pointers to avoid duplicates or move them intelligently.
2. Pointer Movement Logic: Your current approach moves the left pointer forward regardless of whether you find a match or not, and you're resetting it to 0. This doesn't follow the typical two-pointer pattern where you move pointers based on whether your current sum is too high, too low, or just right.
3. Algorithm Structure: The standard three-sum approach usually fixes one element and then uses two pointers on the remaining subarray, rather than trying to use all three as moving pointers simultaneously.
4. Duplicate Handling: Your current approach doesn't handle duplicate results - you'll likely get the same triplet multiple times.

Since we only need unique triplet sets, we can simplify search by using unordered_set, deleting duplicates.

Lets systematically deal issues that I have one by one in the next try...

### Submission Code 2 - w. hints ()


### What I found out to code the approach


## Solutions

### Solution 1
~~~cpp

~~~

Time Complexity: 
Space Complexity: 

### Solution 2
~~~cpp

~~~

Time Complexity: 
Space Complexity: 

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp

~~~