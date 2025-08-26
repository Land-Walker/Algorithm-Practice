# LC Q.853 Car Fleet

2025.08.25. / 08.26

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 23:03 (1st Try) / 20:38 (2nd Try)

End Time: 23:35 (1st Try) / 21:10 (2nd Try)

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

### Submission Code 2 w. help of Grok (Solved...)
~~~cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<double, double>> cars;
        stack<double> timeStack;

        for (int i = 0; i < position.size(); ++i) {
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.begin(), cars.end(), greater<pair<double,double>>());

        for (auto p : cars) {
            double arrivalTime = (target - p.first) / p.second;
            if (!timeStack.empty() && timeStack.top() < arrivalTime) {
                timeStack.push(arrivalTime);
            } else if (timeStack.empty()) {
                timeStack.push(arrivalTime);
            }
        }

        return timeStack.size();
    }
};
~~~

Finally got it...
What was wrong:
- using while (wtf Claude. it was you who said it is necessary.)
  - when you think about it, it's obvious that while does not have to be used here.
  - since pair is used, the while is unnecessary to track position and speed at the same time.
- pop the arrival time of the car, which is unnecessary since we want the cars to form a group/fleet

Still, I need to spend some time to understand the algorithm
- But, I can see the pattern of the stack Q now...
- need deeper study of stack Qs in review notes

Time Complexity: $O(n\log n)$, 56ms, beats 36.73%
Space Complexity: O(n), 89.7MB, beats 33.8%

### What I found out to code the approach
how to use pair
- maybe map can be used?

## Solutions

### Solution 1 (Stack)
~~~cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pair;
        for (int i = 0; i < position.size(); i++) {
            pair.push_back({position[i], speed[i]});
        }
        sort(pair.rbegin(), pair.rend());
        vector<double> stack;
        for (auto& p : pair) {
            stack.push_back((double)(target - p.first) / p.second);
            if (stack.size() >= 2 &&
                stack.back() <= stack[stack.size() - 2])
            {
                stack.pop_back();
            }
        }
        return stack.size();
    }
};
~~~

Time Complexity: $O(n\log n)$
Space Complexity: O(n)

### Solution 2 (Iteration)
~~~cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> pair;
        for (int i = 0; i < n; i++) {
            pair.push_back({position[i], speed[i]});
        }
        sort(pair.rbegin(), pair.rend());

        int fleets = 1;
        double prevTime = (double)(target - pair[0].first) / pair[0].second;
        for (int i = 1; i < n; i++) {
            double currTime = (double)(target - pair[i].first) / pair[i].second;
            if (currTime > prevTime) {
                fleets++;
                prevTime = currTime;
            }
        }
        return fleets;
    }
};
~~~

Time Complexity: $O(n\log n)$
Space Complexity: O(n)

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, float>> cars(n);
        for (int i = 0; i < n; ++i) cars[i] = {position[i], (float)(target - position[i]) / speed[i]};
        sort(cars.begin(), cars.end());
        int fleets = 0;
        float prevTime = 0.0;
        for (int i = n - 1; i >= 0; --i) {
            if (cars[i].second > prevTime) {
                ++fleets;
                prevTime = cars[i].second;
            }
        }
        return fleets;
    }
};
~~~