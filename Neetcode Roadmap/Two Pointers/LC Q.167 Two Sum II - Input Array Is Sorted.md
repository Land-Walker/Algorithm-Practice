# LC Q.167 Two Sum II - Input Array Is Sorted

2025.08.13.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:13

End Time: 22:34

## My Approaches

### Basic Ideas
- Implement two pointer

### Submission Code 1 (Solved)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l = 0;
        int r = numbers.size() - 1;

        while(l < r) {
            if (target > numbers[l] + numbers[r]) {
                l++;
            } else if (target < numbers[l] + numbers[r]) {
                r--;
            } else {
                break;
            }
        }

        res.push_back(l+1);
        res.push_back(r+1);
        return res;
    }
};
~~~

Implemented two pointer learnt from Q125.

Time complexity: O(n), 0ms, beats 100%
Space complexity: O(1)

Nice example to practice two pointers...
But it was way too easy. 
(Exactly same as the solution, except changing the last part as return { l + 1, r + 1 };)

Since I knew how to implement two pointers, the main question is how should I recognize two pointer Qs:
Input Structure:
- Sorted or sortable data (arrays, strings)
- Need to examine elements from both ends
- Looking for pairs, triplets, or ranges
- Problems involving "closest" or "farthest" elements

Problem Constraints:
- Asked to solve in O(n) time instead of O(n²)
- Need to avoid nested loops
- Memory constraints favor in-place solutions
- Problems that seem to require checking all pairs

Language Clues:
- Words like "pair," "two elements," "opposite ends"
- "Closest to target," "maximum/minimum sum"
- "Move inward," "shrink window"
- "Left and right boundaries"

### What I found out to code the approach
How to implement two pointers

## Solutions
No detailed explanation will be written as two pointers method is the optimal method for this one.

### Solution 1
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (numbers[i] + numbers[j] == target) {
                    return { i + 1, j + 1 };
                }
            }
        }
        return {};
    }
};
~~~

Time Complexity: $O(n^2)$
Space Complexity: O(1)

### Solution 2 (Binary Search)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++) {
            int l = i + 1, r = numbers.size() - 1;
            int tmp = target - numbers[i];
            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (numbers[mid] == tmp) {
                    return { i + 1, mid + 1 };
                } else if (numbers[mid] < tmp) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        return {};
    }
};
~~~

Time Complexity: $O(n\log n)$
Space Complexity: O(1)

### Solution 3 (Hash Map)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> mp;
        for (int i = 0; i < numbers.size(); i++) {
            int tmp = target - numbers[i];
            if (mp.count(tmp)) {
                return { mp[tmp], i + 1 };
            }
            mp[numbers[i]] = i + 1;
        }
        return {};
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 4 (Two Pointers)
~~~cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;

        while (l < r) {
            int curSum = numbers[l] + numbers[r];

            if (curSum > target) {
                r--;
            } else if (curSum < target) {
                l++;
            } else {
                return { l + 1, r + 1 };
            }
        }
        return {};
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(1)

### Challenge Solution
No challenge solution since my solution is work well as much as challenge solution (beats 100%)