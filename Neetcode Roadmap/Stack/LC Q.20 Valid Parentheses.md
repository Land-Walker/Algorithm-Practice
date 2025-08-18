# LC Q.20 Valid Parentheses

2025.08.18.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:02

End Time: 22:46

## My Approaches

### Basic Ideas
Alright, lets first google what stack is in C++.
I will add this in AlgoSelfStudy doc, but here is brief summary:
#### Key characteristics of a C++ stack:
**LIFO Principle**:
Elements are added (pushed) and removed (popped) only from one end, known as the "top" of the stack. The last element inserted is the first one to be retrieved.

**Container Adapter**:
std::stack is not a standalone container but an adapter that uses an underlying sequential container (like std::deque by default, std::vector, or std::list) to store its elements.

**Restricted Access**:
Unlike other containers like std::vector, elements in a stack cannot be accessed by their index. Only the top element is directly accessible.

**Common operations and member functions**:
push(element): Adds an element to the top of the stack.
pop(): Removes the element from the top of the stack.
top(): Returns a reference to the top element of the stack without removing it.
empty(): Returns true if the stack is empty, false otherwise.
size(): Returns the number of elements in the stack.

As this Q is classified as stack, I will try to use stack...

### Submission Code 1 w. 3 hints from Leetcode & debugging hint help from ACC (Solved!)
Used stack...
~~~cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> strStack;
        char top {};

        if (s.length() % 2 == 1) {
            return false;
        }

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                strStack.push(c);
            }
            
            if (c == ')') {
                // the if statement that I spent most 
                if (!strStack.empty()) {
                    top = strStack.top();
                } else {
                    return false;
                }

                if (top == '(') {
                    strStack.pop();
                    continue;
                } else {
                    return false;
                }
            }

            if (c == '}') {
                if (!strStack.empty()) {
                    top = strStack.top();
                } else {
                    return false;
                }

                if (top == '{') {
                    strStack.pop();
                    continue;
                } else {
                    return false;
                }
            }

            if (c == ']') {
                if (!strStack.empty()) {
                    top = strStack.top();
                } else {
                    return false;
                }
                
                if (top == '[') {
                    strStack.pop();
                    continue;
                } else {
                    return false;
                }
            }
        }
        
        return strStack.empty();
    }
};
~~~

Time complexity: O(n), 0ms, beats 100%
Space complexity: O(n), 8.73MB, beats 61%

At first, I tried to use stack as a data structure like map or set.
But, I looked at the hints, and found out that stack should rather be used like an algorithm technique, or a RAM (in computer)...

Also, I need to be very careful about stack overflow, as it was main bug that I faced.
- After looking at a hint, it spent 10-15min to implement it, but spent all other times to debug...
- This might be because of its LIFO rule.
- More algorithmic approach is required
  - e.g. when this input comes in, what should happen in stack, etc.

I think I need more practice on stack to master it...

But, nice start of stack Qs!

### What I found out to code the approach
- How to use stack
- you can directly slice a string by: mystring[i]
- DO NOT forget that for (char c : s) is possible...
  - spent a lot of time debugging a data type conversion by using noremal for loop statement (for (int i {}; etc...))

## Solutions

### Solution 1 (Brute Force)
for completeness...
~~~cpp
class Solution {
public:
    bool isValid(string s) {
        while (true) {
            size_t pos = string::npos;
            if ((pos = s.find("()")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            if ((pos = s.find("{}")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            if ((pos = s.find("[]")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            break;
        }
        return s.empty();
    }
};
~~~

Time Complexity: $O(n^2)$
Space Complexity: O(n)

### Solution 2 (Stack)
~~~cpp
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char, char> closeToOpen = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char c : s) {
            if (closeToOpen.count(c)) {
                if (!stack.empty() && stack.top() == closeToOpen[c]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
~~~

Time Complexity: O(n)
Space Complexity: O(n)

Super, super, super smart method, by using } as a key and { as a value...

Check if it is a close brace by using a key, and call a corresponding open brace as a value.

Make everything super simple, and neat, not like my submission code (dirty, many ifs...)

I did think about store it seperately, but my thought didnt reach to the unordered_map...
- Need to remember as it is an amazing application of it...

Oh, I found one better thing about my submission code. 
Mine is better at space complexity as it does not contain a map.

### Challenge Solution
NaN, stack method already beats 100%