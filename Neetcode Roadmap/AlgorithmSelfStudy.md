# README
This note will contain two main things:
1. Technical code bits in C++ to be used in algorithm problem solving
2. Mathematical concepts and details will be mostly from Introduction to Algorithm book

General work flow will be:
1. Solve Leetcode Questions
2. Learn technical coding skills and little background knowledge & Make a note of them here
3. Learn theory behind with Introduciton to Algorithm & Make a note of them here

# Algorithms

## Hashing
### C++
#### std::set
**Ordered container with unique elements**
- Elements are automatically sorted
- No duplicate values allowed
- O(log n) insertion, deletion, and lookup
- Based on balanced binary search tree (typically red-black tree)

~~~cpp
#include <set>
std::set<int> s = {3, 1, 4, 1, 5, 1};
// Result: {1, 3, 4, 5} - sorted, duplicates removed
s.insert(2);
if (s.find(4) != s.end()) {
    std::cout << "Found 4!";
}
~~~

#### std::multiset
**Ordered container that allows duplicate elements**
- Elements are automatically sorted
- Allows multiple copies of the same value
- Based on balanced binary search tree (typically red-black tree)

~~~cpp
#include <set>
std::multiset<int> ms = {3, 1, 4, 1, 5, 1};
// Result: {1, 1, 1, 3, 4, 5} - sorted with duplicates
ms.insert(2);
std::cout << ms.count(1); // Output: 3
~~~

#### std::unordered_set
**Hash table for unique elements with fast access**
- No ordering of elements
- No duplicate values allowed
- Average O(1) insertion, deletion, and lookup
- Based on hash table

~~~cpp
#include <unordered_set>
std::unordered_set<std::string> us = {"apple", "banana", "cherry"};
us.insert("date");
if (us.find("apple") != us.end()) {
    std::cout << "Found apple!";
}
// Elements stored in arbitrary order
~~~

#### std::map
**Ordered key-value pairs with unique keys**
- Keys are automatically sorted
- Each key can appear only once
- O(log n) operations
- Based on balanced binary search tree

~~~cpp
#include <map>
std::map<std::string, int> ages;
ages["Alice"] = 25;
ages["Bob"] = 30;
ages["Charlie"] = 35;
// Keys stored in alphabetical order: Alice, Bob, Charlie
std::cout << ages["Bob"]; // Output: 30
~~~

#### std::unordered_map
**Hash table for key-value pairs with fast access**
- No ordering of key-value pairs
- Unique keys only
- Average O(1) operations
- Based on hash table
- Use most often

~~~cpp
#include <unordered_map>
std::unordered_map<int, std::string> lookup;
lookup[101] = "John";
lookup[205] = "Jane";
lookup[350] = "Bob";
// Keys stored in arbitrary order
if (lookup.find(101) != lookup.end()) {
    std::cout << lookup[101]; // Output: John
}
~~~

#### Quick Comparison
- **Ordered**: `std::set`, `std::multiset`, `std::map` (O(log n) operations)
- **Unordered**: `std::unordered_set`, `std::unordered_map` (O(1) average operations)
- **Allows duplicates**: Only `std::multiset`
- **Unique elements only**: `std::set`, `std::unordered_set`
- **Key-value storage**: `std::map`, `std::unordered_map`

### Math

## Sorting
### C++
#### Bucket Sort

## Heap
### C++
#### std::priority_queue

# Reference
https://velog.io/@gb_leem/C-set-maphash
https://velog.io/@gb_leem/C-list-stack-queue-heap

# Potential Things to Cover
Referred to The Alorithm repo in github:
%%
# Backtracking
# Bit Manipulation
# Ciphers
# CPU Scheduling Algorithms
# Data Structures
# Divide & Conquer
# Dynamic Programming
# Games
# Geometry
# Graph
# Graphics
# Greedy Algorithms
# Machine_Learning
# Math
# Numerical Methods
# Operations on Data Structures
# Physics
# Probability
# Range Queries
# Scripts
# Searching
# Sorting
# Strings
%%