# LC Q.42 Trapping Rain Water

2025.08.16.

Difficulty: #hard

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:36 (1st Try)

End Time: 23:17 (1st Try)

## My Approaches

### Basic Ideas
- Using two pointers, find places where water can be trapped.
- store each vector
- using two pointers again, find the area of water stored in each trap

Looked at the hint in Neetcode.
- for a specific location i, area = min(height[l], height [r]) - height[i]
- 3 pointer from Q15 should be used.
- check l and r at specific location i, and calculate area
- Wait, is two pointer necessary?
- for loop for an i, and calculate area by setting l = i -1 and r = i + 1.
  - Nope, but one thing that I notice during implementing such logic is that I have to use two pointer to find max. l and max. r
  - store maxl & maxr, and calculate at the end of the loop.

### Submission Code 1 w. Hints from Claude/NeetCode (Failed - TLE)
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;

        for (int i{1}; i < height.size() - 1;++i) {
            int l = 0;
            int r = height.size() - 1;
            int maxl = 0;
            int maxr = height.size() - 1;
            
            while (l < i) {
                if (height[maxl] < height[l]) {
                    maxl = l;
                    ++l
                }
            }
            while (r > i) {
                if (height[maxr] < height[r]) {
                    maxr = r;
                }
                --r;
            }
            int area = min(height[maxr], height[maxl]) - height[i];
            if (area > 0) {
                res = res + area;
            }
        }

        return res;
    }
};
~~~
321 / 324 testcases passed...

Few things I changed / added from the first logic implementation (advice from Claude):
- seperate l & r loops
- initialize l, r, maxl, maxr inside of the loop
- set r and maxr as .size() -1, not just .size()...
All of these are stupid mistakes that I made in previous 2 Qs, so I should remind myself for next Q...

TLE is kinda expected, since the process is inefficient.
- finding max could be done outside of for loop maybe...
- No, it will still give $O(n^2)$ time complexity.
- it requires some smart way to operate two pointers

Yes...
I GGed....

### What I found out to code the approach


## Solutions

### Solution 1 (Brute Force)
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }
        int n = height.size();
        int res = 0;

        for (int i = 0; i < n; i++) {
            int leftMax = height[i];
            int rightMax = height[i];

            for (int j = 0; j < i; j++) {
                leftMax = max(leftMax, height[j]);
            }
            for (int j = i + 1; j < n; j++) {
                rightMax = max(rightMax, height[j]);
            }

            res += min(leftMax, rightMax) - height[i];
        }
        return res;
    }
};
~~~

Time Complexity: $O(n^2)$
Space Complexity: O(1)

### Solution 2 (Prefix & Suffix Arrays)
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) {
            return 0;
        }

        vector<int> leftMax(n);
        vector<int> rightMax(n);

        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = max(leftMax[i - 1], height[i]);
        }

        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = max(rightMax[i + 1], height[i]);
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            res += min(leftMax[i], rightMax[i]) - height[i];
        }
        return res;
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 3 (Stack)
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }

        stack<int> stk;
        int res = 0;

        for (int i = 0; i < height.size(); i++) {
            while (!stk.empty() && height[i] >= height[stk.top()]) {
                int mid = height[stk.top()];
                stk.pop();
                if (!stk.empty()) {
                    int right = height[i];
                    int left = height[stk.top()];
                    int h = min(right, left) - mid;
                    int w = i - stk.top() - 1;
                    res += h * w;
                }
            }
            stk.push(i);
        }

        return res;
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 4 (Two Pointers)
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) {
            return 0;
        }

        int l = 0, r = height.size() - 1;
        int leftMax = height[l], rightMax = height[r];
        int res = 0;
        while (l < r) {
            if (leftMax < rightMax) {
                l++;
                leftMax = max(leftMax, height[l]);
                res += leftMax - height[l];
            } else {
                r--;
                rightMax = max(rightMax, height[r]);
                res += rightMax - height[r];
            }
        }
        return res;
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(1)

### Challenge Solution (Two Pointers)
If I get more confident with C++, read this part & try to learn its technique
~~~cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        int left=0,right=n-1;
        int left_max=0,right_max=0,sum=0;

        while(left<right){
            if(height[left]<height[right]){
                if(left_max>height[left]){
                    sum+=left_max-height[left];
                } else left_max=height[left];
                left++;
            } else {
                if(right_max>height[right]){
                    sum+=right_max-height[right];
                } else right_max=height[right];
                right--;
            }
        }
        return sum;
    }
};
~~~