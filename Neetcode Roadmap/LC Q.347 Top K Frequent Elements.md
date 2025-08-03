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
        for (int num : nums) {              //super simple way to add number (key) and its frequency (value) 
            count[num]++;
        }

        vector<pair<int, int>> arr;
        for (const auto& p : count) {       //simple way to shift key / value position (but it is stored as vector instead of map)
            arr.push_back({p.second, p.first});
        }
        sort(arr.rbegin(), arr.rend());     //sort arr in reversing order, which is ascending order

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(arr[i].second);   //same as what I did, store result from sorted arr
        }
        return res;
    }
};
~~~

This is similar method to mine, but neater.
Speed will be similar since this uses vector, while mine uses map but my code is longer
Also, the for loop is used similarly, which largely impacts the speed.

Nah, what I wrote there is wrong according to claude.
**My code is significantly worse than the solution**:
- Inefficient frequency counting: counting is unecessarily complex
- Modifying map during iteration
- Multiple passes: k is passed multiple times, makes hard to follow
- Therefore, my code is slower and kinda terrible at managing.

Yeap, totally agree.

Time Complexity: $O(n\log n)$ (my code was $O(n\times m)$)
Space Complexity: $O(n)$

### Solution 2 (Min-Heap)
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // count frequency of each number
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        // min heap of pairs (frequency, number)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap; //min_heap creation
        for (auto& entry : count) {                 
            heap.push({entry.second, entry.first}); // add (frequency, number) to heap
            if (heap.size() > k) {                  // If heap has more than k elements, remove the one with lowest frequency
                heap.pop();                         // Removes the element with smallest frequency (top of min-heap)
            }
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(heap.top().second);       // gets the number (not frequency)
            heap.pop();                             // Remove this element from heap
        }
        return res;
    }
};
~~~

This guy is just a tree / filter, which automaically organizes key/value pair that you put in ascending / descending order.
Pop literally pops the bubble located at the top or the root of the tree.

Time Complexity: $O(n\log k)$
Space Complexity: $O(n+k)$

### Solution 3 (Bucket Sort)
~~~cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Place to count frequency of each number
        unordered_map<int, int> count;

        // Create buckets for each possible frequency
        vector<vector<int>> freq(nums.size() + 1);      // Size is nums.size() + 1 because max frequency = all elements are the same

        // Count how many times each number appears
        for (int n : nums) {
            count[n] = 1 + count[n];
        }

        // Put each number into the bucket corresponding to its frequency
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);  // Put the number into the bucket at index = its frequency
        }

        vector<int> res;

        //Collect results by going through buckets from highest frequency to lowest
        for (int i = freq.size() - 1; i > 0; --i) { // decrement i to stop whenever res stored enough values
            for (int n : freq[i]) {                 // Process all numbers that have frequency i
                res.push_back(n);                   // Add this number to our result

                // Stop as soon as we have k numbers (the k most frequent)
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
~~~

Details about the bucket sort is in [[AlgorithmSelfStudy.md]]

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