# LC Q.739 Daily Temperatures

2025.08.24.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 15:20 (1st Try), 18:40 (2nd Try)

End Time: 15:53 (1st Try), 19:13 (2nd Try)

## My Approaches

### Basic Ideas
Do I have to use stack in this?
I will try brute force, then try to use stack...
- Oops never mind, brute force requires $O(n^2)$
I will use stack...

Okay, had no idea, and way too tired...
Will come back later and try to solve this with hints from Claude...

### Submission Code 1 w.hints from Claude (Solved...)
~~~cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> index;
        vector<int> res(n);

        
        for (int i{n-1}; i >= 0; --i) {
            while (!index.empty() && temperatures[index.top()] < temperatures[i]) {
                index.pop();
            }

            if (!index.empty()) {
                res[i] = index.top() - i;
            }
            index.push(i);
        }

        return res;
    }
};
~~~

Alright, my brain doesnt really work well now, so will come back tmr
- & dig deeper why I struggled so much
- & understand what is going on...
- (I think my approach/idea about stack in algorithm Qs is wrong)

Came back after looking at the answer.
- This was DP method implemented. (why I struggled... maybe.)
- I do not have to use stack.

Time Complexity: O(n), 7ms, Beats 97.83%
Space Complexity: O(n), 102.88MB, Beats 80.09%

### What I found out to code the approach
the categorization in stack session in neetcode roadmap is trash.

## Solutions

### Solution 1 (Brute Force)
Purely for completeness
~~~cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n);

        for (int i = 0; i < n; i++) {
            int count = 1;
            int j = i + 1;
            while (j < n) {
                if (temperatures[j] > temperatures[i]) {
                    break;
                }
                j++;
                count++;
            }
            count = (j == n) ? 0 : count;
            res[i] = count;
        }
        return res;
    }
};
~~~

Time Complexity: $O(n^2)$
Space Complexity:
- O(1) extra space
- O(n) for output array

### Solution 2 (Stack)
~~~cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n);

        for (int i = 0; i < n; i++) {
            int count = 1;
            int j = i + 1;
            while (j < n) {
                if (temperatures[j] > temperatures[i]) {
                    break;
                }
                j++;
                count++;
            }
            count = (j == n) ? 0 : count;
            res[i] = count;
        }
        return res;
    }
};
~~~

This stack solution is trash.
Got TLE...
- of course... the while loop there will goes forever if temperatures array is long.
- This is one of ideas that I skipped in my head since it is inefficient...

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 3 (Dynamic Programming)
~~~cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);

        for (int i = n - 2; i >= 0; i--) {
            int j = i + 1;
            while (j < n && temperatures[j] <= temperatures[i]) {
                if (res[j] == 0) {
                    j = n;
                    break;
                }
                j += res[j];
            }

            if (j < n) {
                res[i] = j - i;
            }
        }
        return res;
    }
};
~~~

This is very similar to what Ive done with Claude...
- performancewise, it is almost the same
Okay, that's why I struggled to understand algo.
It was because it implemented certain technique that I do not know.

Completely new method.
Will make a note of it in AlgoSelfStudy doc.

Time Complexity: O(n)
Space Complexity:
- O(1) extra space
- O(n) for output array

### Challenge Solution
NaN, Im okay with what I got with Claude's hint...