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
Use iterator in for loop definition

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