# LC Q.150 Evaluate Reverse Polish Notation

2025.08.21.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:41

End Time: 23:36

## My Approaches

### Basic Ideas
1. detect numbers / symbols
2. store each of them in separate stacks
3. calculation is done in for loop with numStack.size()
   1. use numStack.top, pop it, then use symStack.top, pop it, then use numStack.top, pop it, then calculate the number
   2. store the result of this in int res
   3. do the next calculation
4. return res

### Submission Code 1 (Failed)
~~~cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int res {0};
        std::stack<long long> numStack;
        std::stack<string> symStack;

        for (const string& str : tokens) {
            if (!isOperator(str)) {
                long long num = stoll(str);
                numStack.push(num);
            } else {
                symStack.push(str);
            }
        }

        int n = numStack.size();
        for (int i{0}; i < n; ++i) {
            if (i == 0) {
                res = numStack.top();
                numStack.pop();
            }
            
            if (symStack.top() == "+") {
                symStack.pop();
                res = res + numStack.top();
                numStack.pop();
            } else if (symStack.top() == "-") {
                symStack.pop();
                res = res - numStack.top();
                numStack.pop();
            } else if (symStack.top() == "*") {
                symStack.pop();
                res = res * numStack.top();
                numStack.pop();
            } else if (symStack.top() == "/") {
                symStack.pop();
                res = res / numStack.top();
                numStack.pop();
            }
        }

        return res;
    }

    bool isOperator(const string& c) {
        return (c == "+" || c == "-" || c == "*" || c == "/");
    }
};
~~~

The main problem here is the number of iteration in the for loop.
This seems like it can cause some undefined behavior...?
- No, in this algo, when symbol is encountered, it should be calculated right away.
- It should? not be stored in another stack.

Instead, I will try what Grok said.
Use one for loop, one stack.

### Submission Code 2 w.Grok Hint (Failed)
Tried with Grok hint, but not much improvement.

I think my understanding of stack type of question is wrong...

### What I found out to code the approach
- stoll() to convert string to long long

## Solutions

### Solution 1 (Grok Ver. / Stack)
~~~cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> numStack; // Stack to store numbers
        
        for (const string& str : tokens) {
            if (isOperator(str)) {
                // Pop the top two numbers (in reverse order for subtraction/division)
                long long b = numStack.top(); numStack.pop();
                long long a = numStack.top(); numStack.pop();
                
                // Perform the operation
                if (str == "+") {
                    numStack.push(a + b);
                } else if (str == "-") {
                    numStack.push(a - b);
                } else if (str == "*") {
                    numStack.push(a * b);
                } else if (str == "/") {
                    // Check for division by zero
                    if (b == 0) {
                        throw runtime_error("Division by zero");
                    }
                    numStack.push(a / b);
                }
            } else {
                // Convert string to number and push to stack
                numStack.push(stoll(str));
            }
        }
        
        return static_cast<int>(numStack.top());
    }

private:
    bool isOperator(const string& c) {
        return (c == "+" || c == "-" || c == "*" || c == "/");
    }
};
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