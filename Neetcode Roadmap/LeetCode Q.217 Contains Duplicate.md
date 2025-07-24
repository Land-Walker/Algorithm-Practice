# LeetCode Q.217 Contains Duplicate

2025.07.24.

Difficulty: #easy

Type of Algorithm: [Arrrays&Hashing]

Tags:

Start Time: 19:34

End Time: 20:30

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

#### Complexity
Time Complexity: O($n\log n$)
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

- seen is the name of the unordered_set
- single colon, :, is a member initializer
    - it is used when the constructor definition to initialize member variables before the constructor body executes
    - Particularly useful for:
        - **Initializing const members**: const members must be initialized in the initializer list as they cannot be assigned a value later.
        - **Initializing reference members**: Similar to const members, reference members must be initialized in the initializer list.
        - **Calling base class constructors**: When a derived class constructor is called, the base class constructor is called in the initializer list.
        - **Performance optimization**: For complex objects, initializing in the member initializer list can be more efficient than assigning values in the constructor body.

#### Complexity
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
- .begin() & .end() refer to the first and end element in std::vector
    - often use to represent the range of std::vector
    - in this code, nums.begin(), nums.end() basically says to store all of its elements to unordered_set

- Here, we cannot use unordered_map, which is often the most useful hash table
    - This is because map needs keys for each value, which is meaningless & bad for space complexity

#### Complexity
Time Complexity: O(n)
Space Complexity: O(n)