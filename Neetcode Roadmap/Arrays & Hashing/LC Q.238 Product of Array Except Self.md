# LC Q.238 Product of Array Except Self

2025.08.05.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:55 (1st try) 22:28 (2nd try)

End Time: 20:20 (1st try)

## My Approaches

### Basic Ideas
Lets try to design O(n) without using division
1. Need one loop to iterate all nums
    - need idea development, but Im tired and around me is loud, so will solve it later

    - Here I am.
    - Alrigt tried many ways.
    - Most of the time, it requires nested for loops.
    - GG, I cannot think of a way to solve this without division (which makes the Q really, really easy by just divide n[i] after multiply all) or brute force
    - My final idea was using a pointer, one to point starting from i to the end and the other to point from beginning to i
    - Lets see the answers...

### Submission Code 1 (Failed during the prototyping process)
Note that this is just a piece of rough prototype...
~~~cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> key (nums.size());
        unordered_map<int, vector<int>> maps;
        unordered_map<int, int> res;
        vector<int> answer (nums.size(), 1);

        for (int i{0}; i < nums.size(); ++i) {
            (nums.begin() + i)
        }

        for (int j{0}; j < nums.size(); ++j) {
            vector<int>& temp = key;
            temp.erase(temp.begin() + j);
            maps[key[j]] = temp;
            res[key[j]];
        }

        for (int k{0}; k < nums.size()-1; ++k) {
            vector<int>& tempmap = maps[k];
            for (n : tempmap) {
                res[k] = 
            }

        }

        for (pair : res) {
            answer[pair.first] = answer[pair.first] * res[pair.second]
        }
        return ans;

    }
};
~~~

### What I found out to code the approach
- how to initialize vectors inside of map or vector

## Solutions
Skipped Solutions using Brute force or Division, making the Q way too easy
### Solution 1 (Prefix & Suffix)
~~~cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        vector<int> pref(n);
        vector<int> suff(n);

        pref[0] = 1;
        suff[n - 1] = 1;
        for (int i = 1; i < n; i++) {
            pref[i] = nums[i - 1] * pref[i - 1];
        }
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = nums[i + 1] * suff[i + 1];
        }
        for (int i = 0; i < n; i++) {
            res[i] = pref[i] * suff[i];
        }
        return res;
    }
};
~~~

Basically my last idea was right.
Simply iterate two times:
- Prefix stores (2*3*4), by fixing & iterating the position with i defined by for loop
- Suffix is doing direct opposite.

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 2 (Optimal Prefix & Suffix)
~~~cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }


        int postfix = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
};
~~~

Long story short, instead of storing data seperately in prefix / res / suffix, it stores directly onto res.

Time Complexity: O(n)
Space Complexity
- O(1): Extra space
- O(n): Space for the output array

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 1);
        int prefix = 1, suffix = 1;

        for(int i = 0; i < nums.size(); i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        for(int i = nums.size() - 1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
};
~~~