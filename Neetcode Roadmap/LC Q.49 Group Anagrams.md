# LC Q.49 Group Anagrams

2025.06.28.

Difficulty: #easy

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 23:03 (1st try)

End Time: 23:37 (1st try)

## My Approaches

### Basic Ideas
1. Utilize Q242 solution 2: Use two for loops
    - one for assigning string s
    - one for assigning string t
    - check one by one if there are anagram set
    - for string t loop, there is a vector to store the same anagram set
    - for string s loop, there is one big vector to store all same anagram set vector
    - for string t loop, there must be a code to remove strings that are in the same anagram set
      - this was wrong, since remove strings will cause index problems

### Submission Code 1
~~~cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> fullResult = {};
        std::vector<std::string> result = {};
        for (int i{0}; i < strs.size()-1; ++i){
            result.insert(result.end(), strs[i]);
                for (int j{1}; j < strs.size()-1; ++j){
                    std:string s = strs[i];
                    std::string t = strs[j];
                    std::sort(s.begin(), s.end());
                    std::sort(t.begin(), t.end());
                    if (strs[i] == strs[j]) {
                        result.insert(result.end(), strs[j]);
                    }
                }
            fullResult.push_back(result);
            result.clear();
        }
        return fullResult;
    }
};
~~~
- didnt work at all...
- I think the key maybe Q.242 soltion 3.
- using array, this quesiton will be easy & can use hashmap, making necessary searching process much faster

### What I found out to code the approach
- how to add vector to vector

## Solutions

### Solution 1



Time Complexity: 
Space Complexity: 

### Solution 2


Time Complexity: 
Space Complexity: 