# LC Q.853 Car Fleet

2025.08.25.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 23:03 (1st Try)

End Time: 23:35 (1st Try)

## My Approaches

### Basic Ideas
$O(n^2)$ algorithm is easy:
- for loop, iterate for n = position.size()
- nest another for loop, adding speed to position
  - remove the position that reached target
- count the number of fleet/erasing process
- output the count

But, what would be the stack solution?

Alright. Try to solve it with some help of Claude, but it didnt figure its way out.
Also, this Q uses Q739 algo, so I will come back after learning how the solution of it works. 

### Submission Code 1 w. help of Claude (Failed)
~~~cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        stack<double> timeStack;

        for (int i = 0; i < position.size(); ++i) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end(), greater<pair<int,int>>());

        for (auto p : cars) {
            double arrivalTime = (target - p.first) / p.second;
            while (!timeStack.empty() && timeStack.top() > arrivalTime) {
                timeStack.pop();
            }
            timeStack.push(arrivalTime);
        }

        return timeStack.size();
    }
};
~~~

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