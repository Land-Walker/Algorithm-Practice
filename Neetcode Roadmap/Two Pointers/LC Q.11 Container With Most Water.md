# LC Q.11 Container With Most Water

2025.08.15.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 16:08

End Time: 16:13

## My Approaches

### Basic Ideas
No sorting requires.
Use two pointers, calculate the area, store it if it is the largest.

%%
Before I start, I have to write this...
"I have the seat full of water."
"Must be the water."
"Let's add that to the words of wisdom."
%%

### Submission Code 1 (Solved!)
~~~cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int res = 0;
        int area = 0;

        while (l < r) {
            if (height[l] > height[r]) {
                area = (r - l) * height[r];
                if (area > res) res = area;
                --r;
            } else if (height[l] < height[r]) {
                area = (r - l) * height[l];
                if (area > res) res = area;
                ++l;
            } else {
                area = (r - l) * height[l];
                if (area > res) res = area;
                --r;
                ++l;
            }
        }

        return res;
    }
};
~~~

Hey, I think I mastered implementation of two pointers (upto medium level Qs)...!

Time Complexity: $O(n^2)$, 0ms, beats 100%
Space Complexity: $O(1)$, 63mb, beats 47.94%

It is little bit inefficient from line 10 to line 24.
- Need to see the solution and observe how if statements can be optimized

## Solution
skipped Brute Force solution...

### Solution 1 (Two Pointers)
~~~cpp
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int res = 0;

        while (l < r) {
            int area = min(heights[l], heights[r]) * (r - l);
            res = max(res, area);

            if (heights[l] <= heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return res;
    }
};
~~~

Improved Points:
It simplifies with using min() and max(), which is pretty clever...
- Maybe I should consider using std functions more often
Also note that it increments only l not both which is what I did...

### Challenge Solution
NaN in leetcode solution page...