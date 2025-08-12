# LC Q.1 Two Sum

2025.07.29.

Difficulty: #easy

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:18

End Time: 19:56

## My Approaches

### Basic Ideas
1. use unordered hash map
   - then find the value that is the same as requested number - an element

One and only thing that pops up in my head without using two for loops

### Submission Code 1 (Failed)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numsMap(nums.begin(), nums.end());
        for (int i{0}; i < nums.size(); ++i) {
            auto findTarget = numsMap.find(target - numsMap[i]);
            if (findTarget != numsMap.end()) {
                vector<int> result = {i, findTarget};
                return result
            }
        }

    }
};
Several things that I got wrong by Grok:
1. Incorrect unordered_map initialization
2. Incorrect map access
3. Incorrect handling of the found pair
4. Missing semicolon after return result
5. No handling of the case where the same element shouldn't be used twice. (assumed in Q tho)
6. Missing return statement for when no solution is found. (forgot to do :( )

### Submission 2 (Solved w. Grok)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numsMap; // Maps number to its index
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            auto findTarget = numsMap.find(complement);
            if (findTarget != numsMap.end()) {
                return {findTarget->second, i};
            }
            numsMap[nums[i]] = i; // Store current number and its index
        }
        return {}; // Return empty vector if no solution is found
    }
};
~~~
Fuck Yeah. It worked.
3ms, beated 70% by myself.

Estimated Time Complexity: O(n)
Estimated Space Complexity: O(1) -> actually O(n)

### What I found out to code the approach
About the fixed code by Grok, 
- The key of unordered map is the number from the nums vector.
- the value is the index of that number in the nums vector.
  - which is opposite to my thought
  - just figured out why
  - this one operates by 
    1. look if complement is stored in numsMap 
    2. if it is stored, print key (index) from numsMap
    3. if it is not stored, just simply add current value corresponding to index i in nums
  - which is more optimal than my initial idea, as it reduces redundant storing process by adding numbers to numsMap at the last

- findTarget points to a specific key-value pair in the map if the complement (i.e., target - nums[i]) is found, or it equals numsMap.end() if not found.

- The -> operator is used to access members of the key-value pair through the iterator. In an unordered_map, each pair has:
  - first: The key (in this case, the number from nums).
  - second: The value (in this case, the index of that number in nums).
  - So, findTarget->second retrieves the index of the number that matches the complement.

## Solutions
Skipped brute force & sorting
- sorting in neetcode solution was way too complicated, so skipped
### Solution 1 (Two Pass Hash Table)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            hash[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end() && hash[complement] != i) {
                return {i, hash[complement]};
            }
        }
        // If no valid pair is found, return an empty vector
        return {};
    }
};
~~~
In the first iteration:
- add each element's value as a key
- add its index as a value to the hash table

In the second iteration:
- check if each element's complement (target-nums[i]) exists in the hash table
- if does exist, return current element's eindex & its complment's index
- Note that error of identifying the complement as itself must be avoided

In short, it is what I thought for using two for loops

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 2 (One Pass Hash Table)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end()) {
                return {hash[complement], i};
            }
            hash[nums[i]] = i;
        }
        // Return an empty vector if no solution is found
        return {};
    }
};
~~~

Exactly same as my idea, but more neat code.

Time Complexity: O(n)
Space Complexity: O(n)