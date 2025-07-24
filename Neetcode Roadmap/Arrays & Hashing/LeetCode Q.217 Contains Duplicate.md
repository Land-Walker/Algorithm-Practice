# LeetCode Q.217 Contains Duplicate

2025.07.24.

Difficulty: #easy

Type of Algorithm: [Arrrays&Hashing]

Tags:

Start Time: 19:34

End Time:

Link: [Q,217](https://leetcode.com/problems/contains-duplicate/description/)

## My Approaches

### Basic Ideas
Brute force: make 2 loops to check duplicates & return true when duplicate is found

### What I found out to code the approach
Common mistakes:
1. forget to put ; at the end of the statement
2. define the scope of the for loop with {}
3. overflow due to wrong for loop range setting

### Submission Code 1
'''cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for (int i{0}; i < nums.size()-1; ++i) {
            for (int j{i+1}; j < (nums.size()); ++j){
                if (nums[i] == nums[j])
                    return true;
            }
        }
        return false;
    }
};
'''

Passed 70/77 cases / Failed due to Time Limit Exceed

## Solutions
Referred to Neetcode Answers

### Solution 1: Brute Force
Basically the same as my answer, so skip

Time Complexity: O($n^2$)
Space Complexity: O(1)

### Solution 2: Sorting
'''cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
};
'''

1. Sort out numbers in nums
2. Compare numbers in orders, no need to check the first & the last elements etc

Time Complexity: O($n\liog n$)
Space Complexity: O(1) or O(n) depends on the sorting algorithms

### Solution 3: Hash Set
[[AlgorithmSelfStudy^Hash Set|Here]] is the explanation of what hash set is.

'''cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
'''

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 4: Hash Set Length
Using hash set, create the list of non-overlapping elements.
By comparing the length of the hash set and the length of nums, we can easily found out if there is an overlapping element.

'''cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
    }
};
'''

Time Complexity: O(n)
Space Complexity: O(n)

