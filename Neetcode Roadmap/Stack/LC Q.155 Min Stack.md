# LC Q.155 Min Stack

2025.08.20.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 19:57

End Time: 20:18

## My Approaches

### Basic Ideas
This is quite different from other Qs.

It requires me to DESIGN a code that acts like a stack, but with another function called getMin()...

I will use vector as a data structure.

The challenge comes from getMin() function, since a time complexity must be O(1)...
- Alright, find out I cannot even initialize the class...
- This is my first time of designing a class with C++...
- I will write my idea in submission code, and check solution right after...

### Submission Code 1 (No Idea...)
using vector, implement:
- push(): use push_back, send an element to the back of the vector
- pop(): remove the last element of the vector, using myVector.end() iterator
- top(): give the last element of the vector
- getMin(): not sure about O(1) method, but most easy method will be using a for loop
  - So, found out that there is std::min_element() func...!
  - using this, it will be super easy, but still not sure if it is O(1) method
  - min_element() is definitely neat solution, tho

### What I found out to code the approach
- std::min_element(myVector.begin(), myVector.end())

## Solutions

### Solution 1 (Brute Force)
~~~cpp
class MinStack {
public:
    stack<int> stk;
    MinStack() {

    }

    void push(int val) {
        stk.push(val);
    }

    void pop() {
        stk.pop();
    }

    int top() {
        return stk.top();
    }

    int getMin() {
        stack<int> tmp;
        int mini = stk.top();
        while (stk.size()) {
            mini = min(mini, stk.top());
            tmp.push(stk.top());
            stk.pop();
        }

        while (tmp.size()) {
            stk.push(tmp.top());
            tmp.pop();
        }

        return mini;
    }
};
~~~

Alright, suprisingly, it was not cheating to use stack to create stack...
(WTF)

Also, initialization was super simple. Just use self...

Other than that, the logic is similar, and it uses a loop (which is why its brute force)

Time Complexity: O(n) for getMin(), O(1) for others
Space Complexity: O(n) for getMin(), O(1) for others

### Solution 2 (Two Stacks)
~~~cpp
class MinStack {
private:
    std::stack<int> stack;
    std::stack<int> minStack;

public:
    MinStack() {}

    void push(int val) {
        stack.push(val);
        val = std::min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }

    void pop() {
        stack.pop();
        minStack.pop();
    }

    int top() {
        return stack.top();
    }

    int getMin() {
        return minStack.top();
    }
};
~~~

smart logic here is that it uses another stack that stores only min. value.

Time Complexity: O(1), 7ms, Beats 20.03%
Space Complexity: O(n) 23.41MB, Beats 44.18%

### Solution 3 (One Stack)
~~~cpp
class MinStack {
private:
    long min;
    std::stack<long> stack;

public:
    MinStack() {}

    void push(int val) {
        if (stack.empty()) {
            stack.push(0);
            min = val;
        } else {
            stack.push(val - min);
            if (val < min) min = val;
        }
    }

    void pop() {
        if (stack.empty()) return;

        long pop = stack.top();
        stack.pop();

        if (pop < 0) min = min - pop;
    }

    int top() {
        long top = stack.top();
        return (top > 0) ? (top + min) : (int)min;  // checks if top is positive
                                                    // If true: return (top + min) - adds top and min
                                                    // If false: return (int)min - returns min cast to an integer
    }

    int getMin() {
        return (int)min;
    }
};
~~~

Smart, smart approach, by checking if its min. value when a value is pushed.

Time Complexity: O(1), 9ms, Beats 8.83%
Space Complexity: O(n) 23.18MB, Beats 93.59%

### A short reflection of this Q
I should've considered more...
E.g. search what initialization is, and how to do it in C++...

This Q was simple, so my logic was pretty similar to the answer.
But, often what I faced is that my logic changes a lot during implementation process...
Also, the approach of the solutions are not super hard/complex like other Qs, so I might have been figured out getMin() O(1) logic with harder thinking...

(I am writing this since I realized this took only like 30min...)

I am tired now, since some kind of training session is going on in military, but it is still an excuse.
From now on, if I have no idea, I will try to consider at least 30min-1hour...

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
~~~cpp

class MinStack {
public:
    stack<long long> st;
    long long mini;

    MinStack() {}

    void push(int val) {
        if (st.empty()) {
            st.push(val);
            mini = val;
        } else {
            if (val >= mini) {
                st.push(val);
            } else {
                st.push(2LL * val - mini);
                mini = val;
            }
        }
    }

    void pop() {
        if (st.empty()) return;

        long long x = st.top();
        st.pop();

        if (x < mini) {
            // x was encoded, restore old minimum
            mini = 2LL * mini - x;
        }
    }

    int top() {
        if (st.empty()) return -1; // or throw
        long long x = st.top();
        if (x >= mini) return x;
        else return mini; // encoded → real top is mini
    }

    int getMin() {
        return mini;
    }
};
~~~