# LC Q.128 Longest Consecutive Sequence

2025.08.08.

Difficulty: #medium

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:53 (1st try)

End Time: 24:11 (1st try)

## My Approaches

### Basic Ideas
1. Sorting
- store nums to set for sorting and remove duplicate
- spot the place where the difference between two consecutive numbers are not 1
- if all are 1, return the size of the set
- else compare (size of set)- (the found place) and (the found place)
- return largest value

### Submission Code 1 (Failed)
~~~cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> numSet (nums.begin(), nums.end());
        vector<int> position;
        int count{0};
        int res{0};

        if (nums.empty()) {
            return 0;
        }

        for (auto it = numSet.begin(); it != prev(numSet.end()); ++it) {
            auto next_it = next(it);
            if (*it != *next_it -1) {
                position.push_back(count + 1);
            }
            ++count;
        }

        if (position.empty()) {
            return numSet.size();
        }

        int leftNum {0};
        for (int j{0}; j < position.size(); ++j) {
            leftNum = numSet.size() - position[j];
            if (position[j] - res - 1 > res) {
                res = position[j] - res;
            }
        }

        if (leftNum > res) {
            return leftNum;
        } else {
            return res;
        }
    }
};
~~~

Sorting is ok, but the most important 'finding longest sequence' part doesnt work.

Will work in second try.

I hate my code, since it is 
- using prev(), which is higly vulnerable
- method is overcomplicated
- use too many redundant variables, which can be used less with better algorithm

Maybe I shouldnt use set instead of vector?

### What I found out to code the approach
How to use iterator in for loop definition

## Solutions

### Solution 1 (Brute Force)
~~~cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 0;

        // nums are sorted & duplicate is removed.
        unordered_set<int> store(nums.begin(), nums.end());

        // find longest consecutive sequence
        for (int num : nums) {
            int streak = 0, curr = num;
            while (store.find(curr) != store.end()) {   // loop until it meets unexpected number that is not consequtive
                streak++;                               // store the length of the sequence
                curr++;                                 // store next expected consequtive number
            }
            res = max(res, streak);                     // compare if the current calculated sequence is the longest
        }
        return res;
    }
};
~~~

- This method gives TLE, but still useful to learn since it is what I landed (in a wrong way...)
- Actually, this is similar to solution 3, which is what I actually tried to do.

- what I missed is:
  - since it is consequtive sequence, I dont have to track actual numbers in num
  - I can simply create consequtive sequence and check if it matches with the actual num
  - thought way too complicated...

Time Complexity: $O(n^2)$
Space Complexity: O(n)

### Solution 2 (Sorting)
~~~cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(), nums.end());

        int res = 0, curr = nums[0], streak = 0, i = 0;

        // find longest consecutive sequence
        while (i < nums.size()) {
            if (curr != nums[i]) {
                curr = nums[i];
                streak = 0;
            }
            while (i < nums.size() && nums[i] == curr) {
                i++;
            }
            streak++;
            curr++;
            res = max(res, streak);
        }
        return res;
    }
};
~~~

I personally dont like this code.
The core of the code, finding the consecutive sequence is hard to read or follow.
But, in terms of time complexity, there is an improvement...

Time Complexity: $O(n\log n)$
Space Complexity: O(1) or O(n) depending on the sorting algorithm

### Solution 3 (Hash Set)
~~~cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        // find longest consecutive sequence
        for (int num : numSet) {
            if (numSet.find(num - 1) == numSet.end()) {             // check if there is NO lower consecutive number in the set
                int length = 1;
                while (numSet.find(num + length) != numSet.end()) { // increment length & check if there is consecutive number in every iteration
                    length++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};
~~~

Interesting approach in finding longest consecutive sequence:
- By checking if there is no lower consecutive number in the set, it can achieve:
  - Skip meaningless iteration, therefore achieve better time complexity
  - e.g. find 2,3,4,5 sequence in 1,2,3,4,5 set

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 4 (Hash Map)
~~~cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;

        for (int num : nums) {
            if (!mp[num]) {         // Only process if this number hasn't been seen before
                mp[num] = mp[num - 1] + mp[num + 1] + 1;    // Calculate the new sequence length by lower&upper bound sequence length + current char (= 1)
                mp[num - mp[num - 1]] = mp[num];            // Update the left boundary endpoints of the merged sequence
                mp[num + mp[num + 1]] = mp[num];            // Update the right boundary endpoints of the merged sequence
                res = max(res, mp[num]);                    // Update the global maximum
            }
        }
        return res;
    }
};
~~~

For this solution as well, not quite sure if it is better than the solution 3.
In terms of lines, yes, it is more concise.
But in terms of time complexity and readability, I will use the solution 3 instead. (just personal preference...)
(I think worse time complexity is coming from calculating left and right boundary for each iteration.)

Time Complexity: O(n)
Space Complexity: O(n)

### Challenge Solution (Cannot find)