# LC Q.347 Top K Frequent Elements

2025.08.02.

Difficulty: #medium

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 17:16

End Time: 18:02

## My Approaches

### Basic Ideas
1. hashmap
    - use unordered_map, store key & value
    - use for loop with variable k
    - find the key with the highest frequency, store in result vector
    - iterate k times
2. Sorting

### Submission Code 1 (Solved!)
~~~cpp
class Solution {
public:
    int findLargestFreq(unordered_map<int, int>& FreqMap) {
        int largestFreq = 0;
        int largestKey = 0;

        for (const auto& pair : FreqMap) {
            if (pair.second > largestFreq) {
                largestFreq = pair.second;
                largestKey = pair.first;
            }
        }
        FreqMap.erase(largestKey);
        return largestKey;
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;
        vector<int> result;
        
        for (const auto& n : nums) {
            if (!freqMap.count(n)) {
                freqMap[n] = 1;
            } else {
                ++freqMap[n];
            }
        }

        for (int i{0}; i < k; ++i) {
            result.push_back(findLargestFreq(freqMap));
        }
        
        return result;
    }
};
~~~
- worked!!!!!
- Unlike Q1, this is purely my work!!!!! No Grok
- just fantastic.
- All I did is nothing but make my idea real & working
- 4ms, beats 35.02%
- memory beats 95.63%

### What I found out to code the approach
I searched up few things, but they are all trivial and easily understandable with my code.

## Solutions

### Solution 1 (Sorting)
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<pair<int, int>> arr;
        for (const auto& p : count) {
            arr.push_back({p.second, p.first});
        }
        sort(arr.rbegin(), arr.rend());

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(arr[i].second);
        }
        return res;
    }
};
~~~

Time Complexity: $O(n\log n)$
Space Complexity: $O(n)$

### Solution 2 (Min-Heap)
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        for (auto& entry : count) {
            heap.push({entry.second, entry.first});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
        }
    }
};
~~~

Time Complexity: $O(n\log k)$
Space Complexity: $O(n+k)$

### Solution 3 (Bucket Sort)
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (int n : nums) {
            count[n] = 1 + count[n];
        }
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> res;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(n)

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Hash map to count frequencies of each number
        unordered_map<int, int> freq;

        // Count frequencies
        for (int& num : nums)
            freq[num]++; // Increment frequency count for each number

        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            minHeap;
        for (auto& pair : freq) {
            int num = pair.first;
            int count = pair.second;
            minHeap.push({count, num});
            if (minHeap.size() > k)
                minHeap.pop();
        }

        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return result;
    }
};
~~~