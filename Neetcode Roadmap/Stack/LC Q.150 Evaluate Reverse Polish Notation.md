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

Surprisingly, it beats 100%.
My logic was correct, except for the part where I need to pop two top numbers.

%%one weird thing about this code. If I make if statement short, it gives 1ms, beats around 50%. Why is this?%%

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 2 (Stack)
~~~cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        for (const string& c : tokens) {
            if (c == "+") {
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b + a);
            } else if (c == "-") {
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b - a);
            } else if (c == "*") {
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b * a);
            } else if (c == "/") {
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b / a);
            } else {
                stack.push(stoi(c));
            }
        }
        return stack.top();
    }
};
~~~

Basically the same logic, but few different things:
- used int instead of long long (I think this is more vulnerable to overflow)
- initialize a and b every iteration (which takes more memory and makes it slower)
  - But, do not need to make a isOperator function like I did

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 3 (Brute Force)
~~~cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        while (tokens.size() > 1) {
            for (int i = 0; i < tokens.size(); i++) {
                if (tokens[i] == "+"
                    || tokens[i] == "-"
                    || tokens[i] == "*"
                    || tokens[i] == "/")
                {
                    int a = stoi(tokens[i - 2]);
                    int b = stoi(tokens[i - 1]);
                    int result = 0;
                    if (tokens[i] == "+") result = a + b;
                    else if (tokens[i] == "-") result = a - b;
                    else if (tokens[i] == "*") result = a * b;
                    else if (tokens[i] == "/") result = a / b;

                    tokens.erase(tokens.begin() + i - 2, tokens.begin() + i + 1);
                    tokens.insert(tokens.begin() + i - 2, to_string(result));
                    break;
                }
            }
        }
        return stoi(tokens[0]);
    }
};
~~~

Okay, I see. I used Brute force + stack method.
Thats why it didnt work so well.
Brute force do not have efficient data storage method, so it uses res variable.
I do not need to do it, since I have stack, which is much better way to store calculation results.

Time Complexity: $O(n^2)$
Space Complexity: O(n)

### Solution 4 (Doubly Linked List)
~~~cpp
// Custom doubly linked list node for storing RPN tokens
class DoublyLinkedList {
public:
    string val;                    // Stores token (number or operator)
    DoublyLinkedList* next;        // Pointer to next node
    DoublyLinkedList* prev;        // Pointer to previous node
    
    // Constructor: creates node with value and optional next/prev pointers
    DoublyLinkedList(string val, DoublyLinkedList* next = nullptr,
                        DoublyLinkedList* prev = nullptr) {
        this->val = val;
        this->next = next;
        this->prev = prev;
    }
};

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // STEP 1: Build doubly linked list from tokens
        DoublyLinkedList* head = new DoublyLinkedList(tokens[0]);  // Create first node
        DoublyLinkedList* curr = head;                             // Track current position
        
        // Link remaining tokens into doubly linked list
        for (int i = 1; i < tokens.size(); i++) {
            curr->next = new DoublyLinkedList(tokens[i], nullptr, curr);  // Create new node, link bidirectionally
            curr = curr->next;                                            // Move to new node
        }
        
        int ans = 0;  // Will store final result
        
        // STEP 2: Process list left-to-right, evaluating operators in-place
        while (head != nullptr) {
            // Check if current node is an operator
            if (head->val == "+" ||
                 head->val == "-" ||
                 head->val == "*" ||
                 head->val == "/")
            {
                // Extract operands from 2 nodes to the left
                int l = stoi(head->prev->prev->val);  // Left operand (2 positions back)
                int r = stoi(head->prev->val);        // Right operand (1 position back)
                int res = 0;
                
                // Perform the operation
                if (head->val == "+") {
                    res = l + r;
                } else if (head->val == "-") {
                    res = l - r;
                } else if (head->val == "*") {
                    res = l * r;
                } else {
                    res = l / r;
                }
                
                // Replace operator with result and remove consumed operands
                head->val = to_string(res);                    // Store result in current node
                head->prev = head->prev->prev->prev;           // Skip over the 2 consumed operands
                if (head->prev != nullptr) {
                    head->prev->next = head;                   // Update forward link
                }
            }
            
            // Keep track of the last processed value (will be final result)
            ans = stoi(head->val);
            head = head->next;  // Move to next node
        }
        
        return ans;  // Return final computed result
    }
};
~~~

Completely new method 1.
Will make a note of it in AlgoSelfStudy doc.

Time Complexity: O(n)
Space Complexity: O(n)

### Solution 5 (Recursion)
~~~cpp
class Solution {
public:
    int dfs(vector<string>& tokens) {
        // Process tokens from RIGHT to LEFT (reverse of typical RPN)
        string token = tokens.back();  // Get rightmost token
        tokens.pop_back();             // Remove it from vector (destructive parsing)
        
        // BASE CASE: If token is a number, return its value
        if (token != "+" && token != "-" &&
             token != "*" && token != "/")
        {
            return stoi(token);  // Convert string to integer and return
        }
        
        // RECURSIVE CASE: Token is an operator
        // KEY INSIGHT: In RPN processed right-to-left, operands appear in reverse order
        int right = dfs(tokens);  // First recursive call gets RIGHT operand
        int left = dfs(tokens);   // Second recursive call gets LEFT operand
        
        // Perform the operation with correct operand order
        if (token == "+") {
            return left + right;
        } else if (token == "-") {
            return left - right;  // Important: left - right, not right - left
        } else if (token == "*") {
            return left * right;
        } else {
            return left / right;   // Important: left / right, not right / left
        }
    }
    
    int evalRPN(vector<string>& tokens) {
        return dfs(tokens);  // Start recursive evaluation
    }
};
~~~

Completely new method 2.
Will make a note of it in AlgoSelfStudy doc.

Time Complexity: O(n)
Space Complexity: O(n)

### Challenge Solution
NaN, Grok ver. solution already beats 100%