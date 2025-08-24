# README
This note will contain two main things:
1. Technical code bits in C++ to be used in algorithm problem solving
2. Mathematical concepts and details will be mostly from Introduction to Algorithm book

General work flow will be:
1. Solve Leetcode Questions
2. Learn technical coding skills and little background knowledge & Make a note of them here
3. Learn theory behind with Introduciton to Algorithm & Make a note of them here

# Algorithms

# Hashing
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

# Sorting
## Bucket Sort
Instead of sorting things directly,
1. create buckets (usually n * value / range) & put datas into each corresponding bucket
2. sort each bucket
3. combine all buckets

**Time Complexity**
- Best/Average Case: O(n + k) where n = elements, k = buckets
- Worst Case: O(n²) when all elements go into one bucket
- Space: O(n + k)

**When to Use Bucket Sort**
Good for:
- Floating-point numbers in a known range
- Uniformly distributed data
- When you can predict the distribution pattern

Not good for:
- Data with unknown or wide ranges
- Non-uniformly distributed data
- Small datasets (overhead isn't worth it)

### C++
Look at Q347 for C++ Implementation

# Data Structures
## Heap
**Structure**: Complete binary tree - all levels are filled except possibly the last level, which is filled from left to right.

**Property**: For any node at index i, its value ≤ values of its children.

**Array Representation**
For a node at index i:
- Left child: 2*i + 1
- Right child: 2*i + 2
- Parent: (i-1)/2

**Core Operations**
- Insert (Push): Add element at the end, then "bubble up" by comparing with parent and swapping if necessary until heap property is restored.
- Extract Min (Pop): Remove root, replace with last element, then "bubble down" by comparing with children and swapping with the smaller child until heap property is restored.
- Peek: Return the root element (minimum) without removing it.

**Time Complexities**
- Insert: O(log n)
- Extract Min: O(log n)
- Peek: O(1)
- Build heap from array: O(n)

### C++
#### std::priority_queue
To create min-heap:
~~~cpp
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
~~~

To create max-heap:
~~~cpp
std::priority_queue<int> max_heap;
~~~

Operations:
~~~cpp 
bubbleUp(int index)    //Insertion

bubbleDown(int index)  //Extraction

//Navigation
getParent(int index)
getLeftChild(int index)
getRightChild(int index)
~~~

## Bitmask
Definition: uses the individual bits of an integer as a compact way to store a set of boolean flags or represent subsets.

Core Concept: Instead of using arrays, sets, or maps to track "presence/absence" of elements, you use bit positions in an integer.

Analysis of Bitmask
- Super fast:
  - Bitwise operations are among fastest CPU instructions
  - No cache misses from pointer chasing (a.k.a. memory efficient)
  - Parallel operations on multiple bits

- Operations: Set operations become bitwise operations
  - Union: a | b
  - Intersection: a & b
  - Difference: a & ~b

Classic Applications
- Subset enumeration (your Sudoku solution)
- Dynamic programming on subsets (TSP, assignment problems)
- State compression in games/puzzles
- Bloom filters and probabilistic data structures
- Bit manipulation in competitive programming

## Stack



# Doubly Linked List
Q150

# Recursion
Q150


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
# Strings
%%