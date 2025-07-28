# LC Q.242 Valid Anagram

2025.07.27.

Difficulty: #easy

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:51 (1st try) / 23:10 (2nd try)

End Time: 20:19 (1st try) / 23:41 (2nd try)

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
- how to directly sort string

### Submission Code 1
~~~cpp
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
~~~
Tried to use hash table, but failed due to error in pointer

### Submission Code 2
~~~cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        if (s == t) {
            return true;
        }
        return false;
    }
};
~~~
- use direct sorting of std::string
- time taken to solve is 7ms, which is not ideal

## Solutions

### Solution 1 (Sorting)
Logic is basically the same, but this one optimized a bit more:
~~~cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return s == t;
    }
};
~~~
- improved time by 6ms

Time Complexity: $O(n\log n+m\log m)$
Space Complexity: $O(1)$ or $O(n+m)$ depends on the sorting algorithms

### Solution 2 (Hash Map)
In a hash map, store an individual character as a key & a frequency of it as a value
~~~cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> countS;
        unordered_map<char, int> countT;
        for (int i = 0; i < s.length(); i++) {
            countS[s[i]]++;
            countT[t[i]]++;
        }
        return countS == countT;
    }
};
~~~
1. check if the length matches (make it faster a bit, not necessary)
2. initialize countS & countT as an unordered map
3. Increments the count of the character s[i] in countS 
    - If the character isn’t in the map yet, it’s added with an initial count of 1
4. Do similar thing for countT
5. Returns the comparison result

Time Complexity: $O(n+m)$
Space Complexity: $O(1)$

### Solution 3 (Hash Map using array)
The concept is the same with solution 2, but using array instead of hashmap

~~~cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> count(26, 0);
        for (int i = 0; i < s.length(); ++i) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
};
~~~
- this checks if s and t match by adding number of alphabet in s, and substracting number of alphabet in s.
- by finally checking if the count is zero for all alphabet, it works
- not detailed explanation, since this solution is pretty bad compared to solution 2 (personal thought)

Time Complexity: $O(n+m)$
Space Complexity: $O(1)$