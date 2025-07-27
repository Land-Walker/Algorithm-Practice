# LC Q.242 Valid Anagram

2025.07.27.

Difficulty: #easy

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:51 (1st try)

End Time: 20:19 (1st try)

## My Approaches

### Basic Ideas
1. Sort s and t & Compare strings
2. Use hash table (multiset)

second method will be slightly faster
tried second method, but somehow pointer doesnt work properly.
need to do first method instead, and check if direct string sorting is possible

for today (7/27), lets end here for time constraint, and visit tmr.


### What I found out to code the approach
- how to slice string
- std::advance
- .insert()
- .begin() for multiset pointer

### Submission Code 1
'''cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::multiset<std::string> msS;
        std::multiset<std::string> msT;
        for (int i{0}; i < s.size(); ++i) {
             msS.insert(s.substr(i));
             msT.insert(t.substr(i));
        }
        auto ptrS = msS.begin();
        auto ptrT = msT.begin();
        for (int j{0}; j < s.size(); ++j) {
            if (*ptrS != *ptrT)
                return false;
            std::advance(ptrS, 1);
            std::advance(ptrT, 1);
        }
        return true;
    }
};
'''
Tried to use hash table, but failed due to error in pointer

### Submission Code 2


## Solutions

### Solution 1


### Solution 2


