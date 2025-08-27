# LC Q.84 Largest Rectangle in Histogram

2025.08.27.

Difficulty: #hard

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:39 (1st Try)

End Time: 23:32 (1st Try)

## My Approaches

### Basic Ideas
area = min(heights[i], heights[j]) * (heights[j] - heights[i])
- need to find largest consequtive number set

Nope, that is not what the hint from Neetcode says:
- height[i] * (right - left + 1)
- just need to find right and left boundaries
- two pointer? UMM maybe
  - lets try to implement what Ive done in Q42
  - try to use two pointer, but it doesnt fit well
  - Found stack solution, and try to implement that in here.

### Submission Code 1 w. Hints from Claude (Failed)
~~~cpp
if (!stk.empty()) {
    area = heights[popIndex] * (heights.size() - stk.top() - 1);
} else {
    area = heights[popIndex] * heights.size();
}
~~~

DO NOT use CLAUDE for CODING
Makes me so confused.
Will comeback tmr...

still, the main logic is correct, meaning my approach of using Q42 is correct.

### What I found out to code the approach


## Solutions

### Solution 1
~~~cpp

~~~

Time Complexity: 
Space Complexity: 

### Solution 2
~~~cpp

~~~

Time Complexity: 
Space Complexity: 

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp

~~~