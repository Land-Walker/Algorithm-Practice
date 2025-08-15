# LC Q.15 3Sum

2025.08.13. / 08.14. / 08.15.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:50 (1st Try), 22:30 (2nd Try), 15:38 (3rd Try)

End Time: 23:37 (1st Try), 23:23 (2nd Try), 16:07 (3rd Try)

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

Lets  deal issues that I have one by one in the next try...

### Submission Code 2 - w. hints (TLE)
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
  - got close in 2nd try, but still fail in 210/314 test cases...

### Submission Code 4 - w. Hints (Solved!)
~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        vector<vector<int>> resVect;
        int n = nums.size();

        for (int i{0}; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

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
                    while (l < r && l > 0 && nums[l] == nums[l - 1]) {
                        ++l;
                    }
                    while (l < r && r < n-1 && nums[r] == nums[r + 1]) {
                        --r;
                }
                }
            }
        }

        return resVect;
    }
};
~~~

Few hints from claude, but it was mostly making sure my logic is correct & small mistakes that I missed...
- e.g. use while instead of if to skip multiple duplicates

Result)
- Time complexity: $O(n^2)$, beats 73.44%
- Space complexity: $O(n)$, beats 89.69%

One thing that I note is that two pointer is faster/ more memory-efficient than the complexities represent.

### What I found out to code the approach
- super simple way to remove duplicates
- how/when to implement two pointers (what preparation is required to use two pointer technique, etc.)

## Solutions
All solutions in here are for completeness.
The optimal solution is two pointer, which is exactly same as my answer.
- So, I only included non-two pointer solutions.
- 
### Solution 1 (Brute Force)
~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        res.insert({nums[i], nums[j], nums[k]});
                    }
                }
            }
        }
        return vector<vector<int>>(res.begin(), res.end());
    }
};
~~~

Time Complexity: $O(n^3)$
Space Complexity: O(m) (m = number of triplets)

### Solution 2 (Hash Map)
~~~cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); i++) {
            count[nums[i]]--;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < nums.size(); j++) {
                count[nums[j]]--;
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int target = -(nums[i] + nums[j]);
                if (count[target] > 0) {
                    res.push_back({nums[i], nums[j], target});
                }
            }

            for (int j = i + 1; j < nums.size(); j++) {
                count[nums[j]]++;
            }
        }

        return res;
    }
};
~~~

Time Complexity: $O(n^2)$
Space Complexity: O(n) (n = numbers of arrays)

### Challenge Solution
NaN in leetcode solution page...