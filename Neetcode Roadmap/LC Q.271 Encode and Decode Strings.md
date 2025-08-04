# LC Q.271 Encode and Decode Strings

2025.06.04.

Difficulty: #medium

Type of Algorithm: [Array&hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:19 

End Time: 20:19

## My Approaches

### Basic Ideas
1. Simple Brute Force
- Encode: Combine all elements (with whitespace included in between)
- Decode: Seperate elements with whitespaces and store it into a vector

2. Hashing

### Submission Code 1 (Failed)
Tried Brute Force
~~~cpp
class Solution {
public:

    string encode(vector<string>& strs) {
        string res{};

        for (int i{0}; i < strs.size(); ++i) {
            res = res + ' ' + strs[i];
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> res{};

        getline(cin, s);                // get all strings with whitespaces
        stringstream ss(s);             // create a stringstream of s to manipulate s
        string element;                 // create a bucket to store each element in s

        while (ss >> element) {         // >> operator put each element one by one to a bucket
            res.push_back(element);     // add elements to result
        }

        return res;
    }
};
~~~

- Worked well for test cases, but cannot deal with special cases like [] or [""]
- Tried to deal those cases with if statements, but it gets unpretty & inflexible

- can hash map deal with these special cases?
- Maybe this uses some techniques that I dont know yet

- Looked at the hint
- It says use length to represent each string & use # as a seperator
- But, it cannot handle special cases or can it?
- Maybe... but not quite sure

- Think I have to jump straight into the solutions 

### What I found out to code the approach
- How to add strings
- How to seperate strings combined with whitespaces

## Solutions

### Solution 1
~~~cpp
class Solution {
public:
    string encode(vector<string>& strs) {
        // Handle empty input case
        if (strs.empty()) return "";
        
        vector<int> sizes;
        string res = "";

        // Store the length of each string
        for (string& s : strs) {
            sizes.push_back(s.size());
        }

        // Encode all lengths at the beginning, separated by commas (Example: ["hello", "world", ""] -> "5,5,0,#helloworld")
        for (int sz : sizes) {
            res += to_string(sz) + ',';
        }
        res += '#';                     // To add # to mark the start of actual string

        // Concatenate all original strings
        for (string& s : strs) {
            res += s;
        }
        return res;
    }

    vector<string> decode(string s) {
        // Handle empty input case
        if (s.empty()) return {};

        vector<int> sizes;
        vector<string> res;
        int i = 0;                      // Position tracker in encoded string

        // Store all the string lengths (before the '#' separator)
        while (s[i] != '#') {
            string cur = "";
            while (s[i] != ',') {
                cur += s[i];
                i++;
            }
            sizes.push_back(stoi(cur));
            i++;
        }

        // Skip the '#' separator to get to the actual string data
        i++;

        // Extract each string using the lengths we parsed
        for (int sz : sizes) {
            res.push_back(s.substr(i, sz));     // substr(start_pos, length)
            i += sz;                            // Move position forward by the length of string we just extracted
        }
        return res;
    }
};
~~~

Surprisingly simple.
- If I wasn't running out of time, I might be solve this one (due to other things to do after this)
- Need to think more efficient way to do at the beginning, not easy one to implement

Time Complexity: O(m) for each encode() and decode() function calls.
Space Complexity: O(m+n) for each encode() and decode() function calls.

### Solution 2
~~~cpp
class Solution {
public:
    string encode(vector<string>& strs) {
        // Super simple way to encode it as "length#string"
        string res;
        
        for (const string& s : strs) {
            res += to_string(s.size()) + "#" + s;
        }
        
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;

        // Process each encoded segment until we've consumed the entire string
        while (i < s.size()) {
            int j = i;

            // Find the '#' separator to extract the length
            while (s[j] != '#') {
                j++;
            }

            // Extract and convert the length
            int length = stoi(s.substr(i, j - i));      // stoi = C++ standard library function converting string to integer

            // Move past the '#' to start of actual string content
            i = j + 1;

            // Convert length substring to integer
            j = i + length;                             // j now points to position right after this string ends
            res.push_back(s.substr(i, length));         // Extract string of exact length

            // Move to start of next encoded segment
            i = j;
        }

        return res;
    }
};
~~~

Optimized (codewise) version of before

Time Complexity: O(m) for each encode() and decode() function calls.
Space Complexity: O(m+n) for each encode() and decode() function calls.

As you noticed, there is no improvement in complexity.

### Challenge Solution
For this Q, there is no challenge solution to write
- since I solved this one via neetcode, not Leetcode which requires Premium to unlock this Q.