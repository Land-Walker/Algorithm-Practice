# LC Q.125 Valid Palindrome

2025.08.12.

Difficulty: #easy

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:52

End Time: 20:23

## My Approaches

### Basic Ideas
What should I do:
- remove any irrelevant chars
- reverse it and check if it is the same as before

What technique that I can use:
- nothing really...
- maybe two pointers, that checks forward and back at the same time
- but dont know exact algorithm implementation yet
- I will try to implement the vague concept of it, if possible

### Submission Code 1 -(Solved!)
~~~cpp
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> phrase;
        int sNum = 0;
        int revIndex = 0;

        for (char str : s) {
            sNum = static_cast<int>(str);
            if (64 < sNum && sNum < 91) {
                phrase.push_back(tolower(str));
            } else if (96 < sNum && sNum < 123) {
                phrase.push_back(str);
            } else if (47 < sNum && sNum < 58) {
                phrase.push_back(str);
            } else {
                continue;
            }
        }

        for (int i{0}; i < phrase.size(); ++i) {
            revIndex = phrase.size() - i - 1;
            if (phrase[i] != phrase[revIndex]) {
                return false;
            }
        }

        return true;
    }
};
~~~

Time Complexity: O(n), but bad O(n) due to redundancy in the code
- 155ms, beats 6.71%
Space Complexity: O(n)

- tried to use switch case, but it wont be concise as this
- I think I used the concept of two pointer in the second loop.
- Let's see the solution.
- Parts that are too complex:
  - removing redundant characters part.
  - reversing the phrase vector (should I even have to use vector?)
- Must be a better way to solve it...
  - especially solving directly with strings

### What I found out to code the approach
- ASCII code for upper, lower alphabets and numbers

## Solutions

### Solution 1 (Brute Force - Reversing String)
~~~cpp
class Solution {
public:
    bool isPalindrome(string s) {
        string newStr = "";
        for (char c : s) {
            if (isalnum(c)) {
                newStr += tolower(c);
            }
        }
        return newStr == string(newStr.rbegin(), newStr.rend());
    }
};
~~~

Two techniques that I didn't know:
- isalnum(char) to check if the char is alphabet or num (no need for the first part)
- rbegin() and rend() reverse the string very simply... (no need for the second part as well)

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 2 (Two Pointers)
~~~cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0                   // Left pointer starts at beginning
        int r = s.length() - 1;     // Right pointer starts at end

        // Continue until pointers meet or cross over
        while (l < r) {
            while (l < r && !alphaNum(s[l])) {      // Move left pointer forward until we find a valid character
                l++;
            }
            while (r > l && !alphaNum(s[r])) {      // Move right pointer backward until we find a valid character
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])) {   // Convert both to lowercase and compare
                return false;
            }
            l++; r--;                                // continue checking next pair
        }
        return true;
    }

    bool alphaNum(char c) {             // hand-made simple isalnum() function
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
};
~~~

Super simple...
Even though it uses many while loops, it is fast since they are all simple calculations

Also note that there is hand-made simple isalnum() function... much more efficient than mine...
(Yeap, I dont even have to use ASCII code and data type conversion...)

Time Complexity: O(n)
Space Complexity: O(1)

### Challenge Solution (Optimized Two Pointers)
If I get more confident with C++, read this part & try to learn its technique
~~~cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !isalnum(s[left])) left++;
            while (left < right && !isalnum(s[right])) right--;

            if (tolower(s[left]) != tolower(s[right]))
                return false;

            left++;
            right--;
        }

        return true;
    }
};
~~~