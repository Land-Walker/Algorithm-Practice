# LC Q.15 3Sum

2025.08.13. / 08.14.

Difficulty: #easy

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:50 (1st Try), 22:30 (2nd Try), 23:34 (3rd Try)

End Time: 23:37 (1st Try), 23:23 (2nd Try), 

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

Since we only need unique triplet sets, we can simplify search by using set, deleting duplicates.

Lets systematically deal issues that I have one by one in the next try...

### Submission Code 2 - w. hints (TLE)
Issue 1: this can be dealt with unordered_set or sort(). 
- Since unordered_set deletes duplicates and sorts numbers, lets use set.

Issue 2: Since numbers are ordered in set, it will be possible to use similar approach as Q167


~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        vector<vector<int>> resVect;
        int n = nums.size();

        for (int i{0}; i < n; ++i) {
            int l = i + 1;
            int r = n -1;

            // two pointer
            while (l < r) {
                if (nums[i] + nums[r] + nums[l] < 0) {
                    ++l;
                } else if (nums[i] + nums[r] + nums[l]) {
                    --r;
                } else {
                    res = {nums[i], nums[r], nums[l]};
                    sort(res.begin(), res.end());
                    resVect.push_back(res);
                    ++l;
                    --r;
                }
            }
        }

        // super simple way to remove duplicates
        sort(resVect.begin(), resVect.end());
        auto lastUnique = unique(resVect.begin(), resVect.end());
        resVect.erase(lastUnique, resVect.end());

        return resVect;
    }
};
~~~

Gives TLE...

Hint from Claude: I dont have to sort res, since it is already sorted (always check the whole code after I modified it...)

### Submission Code 3 - w. Hints (Solved!)
~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        vector<vector<int>> resVect;
        int n = nums.size();

        for (int i{0}; i < n; ++i) {
            int l = i + 1;
            int r = n -1;

            // two pointer
            while (l < r) {
                if (nums[i] + nums[r] + nums[l] < 0) {
                    ++l;
                } else if (nums[i] + nums[r] + nums[l]) {
                    --r;
                } else {
                    res = {nums[i], nums[r], nums[l]};
                    resVect.push_back(res);
                    ++l;
                    --r;
                }
            }
        }

        // super simple way to remove duplicates
        sort(resVect.begin(), resVect.end());
        auto lastUnique = unique(resVect.begin(), resVect.end());
        resVect.erase(lastUnique, resVect.end());

        return resVect;
    }
};
~~~

Yeap, solved but with:
- Poor time complexity: 2998ms, beats 5% ($O(n^2)$)
- Poor space complexity: 447MB, beats 5%

Main reason for these might be removing duplicates in long vectors...

Hint from claude:
- Can I just skip duplicates during the pointing process?

### What I found out to code the approach
- super simple way to remove duplicates
- 

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