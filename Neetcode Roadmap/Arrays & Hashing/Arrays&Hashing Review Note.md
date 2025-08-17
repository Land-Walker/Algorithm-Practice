# Arrays & Hashing Review Note

2025.08.17

## Overview
- **Total Problems Solved**: 9/9
- **Difficulty Distribution**: Easy (3), Medium (6), Hard (0)
- **Study Period**: 2025.07.24 - 2025.08.08
- **Overall Confidence Level**: 7/10

### One Sentence Review of Each Qs
- **Q.217 (Contains Duplicate)**: First problem - learned hash set basics, brute force TLE taught importance of O(n) solutions
- **Q.242 (Valid Anagram)**: Sorting vs hash map comparison, discovered multiple approaches with same complexity
- **Q.1 (Two Sum)**: Classic hash map problem, learned one-pass vs two-pass techniques and complement searching
- **Q.49 (Group Anagrams)**: Advanced hash map with custom key generation - sorting strings vs frequency counting
- **Q.347 (Top K Frequent Elements)**: First successful solo medium solve, compared hash map + sorting vs heap vs bucket sort
- **Q.238 (Product of Array Except Self)**: Prefix/suffix array technique without division constraint
- **Q.271 (Encode and Decode Strings)**: String manipulation with length encoding - elegant solution using "#" separator  
- **Q.128 (Longest Consecutive Sequence)**: Hash set optimization - learned to start sequences only at sequence beginnings
- **Q.36 (Valid Sudoku)**: Bitmask introduction, multiple constraint checking with hash sets and maps

## Quick Reference (for interviews)
### Problem Type Indicators
- Frequency counting → Hash map/set
- Duplicate detection → Hash set
- Grouping similar items → Hash map with custom keys
- Array problems with O(n) time requirement → Hash map likely
- "Unique", "distinct", "count occurrences" → Hash table approach

### Time Complexity Cheat Sheet
- Hash operations: O(1) average, O(n) worst case
- Hash map solutions: O(n) typical
- Brute force alternatives: O(n²) or O(n log n) with sorting
- Bucket sort optimization: O(n) when range is known

## Core Concepts & Techniques

### Key Data Structures Used
- Primary: `unordered_map<key, value>`, `unordered_set<element>`
- Secondary: `vector`, `set` (for ordered data), arrays for frequency counting
- When to use: Frequency counting, duplicate detection, grouping, O(1) lookups

### Essential Algorithms/Patterns
1. **Frequency Counting**: Store element frequencies in hash map
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - When to apply: Anagrams, top-k problems, duplicate detection
   - Key implementation: `count[element]++` pattern

2. **Complement Search**: Search for target-element in hash map
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - When to apply: Two sum, pair finding problems
   - Key implementation: One-pass with `hash[complement]` checking

3. **Custom Key Generation**: Transform elements into comparable keys
   - Time Complexity: O(n*k) where k is transformation cost
   - Space Complexity: O(n)
   - When to apply: Grouping problems (anagrams, similar strings)
   - Key implementation: Sorted strings or frequency arrays as keys

4. **Bucket Sort**: Use hash frequency + array indexing for O(n) sorting
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - When to apply: Top-k problems with known value range
   - Key implementation: `freq[frequency].push_back(element)`

### C++ Technical Skills Learned
- `unordered_map` vs `unordered_set` selection based on key-value vs element storage
- `.count()` method for existence checking
- `auto&` and `const auto&` for efficient iteration without copying
- `.find() != map.end()` pattern for safe lookups
- Iterator usage and pair access (`.first`, `.second`)
- String manipulation with `to_string()` and `substr()`

## Problem Analysis

### Easiest Problems
- **Q.217 (Contains Duplicate)**: Hash set length comparison - elegant one-liner solution
- **Q.1 (Two Sum)**: Classic problem, straightforward once hash map pattern understood
- **Q.242 (Valid Anagram)**: Multiple clear approaches available
- Common characteristics: Direct hash map application, well-known patterns

### Most Challenging Problems
- **Q.49 (Group Anagrams)**: Required understanding of custom key generation with frequency counting
- **Q.128 (Longest Consecutive Sequence)**: Needed insight to start sequences at beginning elements only
- **Q.36 (Valid Sudoku)**: Complex constraint checking and bitmask introduction
- Key insights: Hash map keys can be complex (strings, coordinates), optimization requires avoiding redundant work

## Pattern Recognition

### How to quickly identify this topic's problems
- **Keywords**: "unique", "duplicate", "frequency", "count", "group", "anagram", "contains"
- **Input characteristics**: Arrays needing grouping, duplicate detection, or frequency analysis
- **Constraint clues**: O(n) time requirement, follow-up asking for better than O(n log n)
- **Problem types**: Counting problems, grouping problems, lookup optimization

## Implementation Templates

### Core Code Patterns
```cpp
// Template 1: Frequency Counting
unordered_map<int, int> count;
for (int num : nums) {
    count[num]++;
}
// Process based on frequencies
```

```cpp
// Template 2: One-Pass Hash Map (Two Sum pattern)
unordered_map<int, int> hash;
for (int i = 0; i < nums.size(); i++) {
    int complement = target - nums[i];
    if (hash.find(complement) != hash.end()) {
        return {hash[complement], i};
    }
    hash[nums[i]] = i;
}
```

```cpp
// Template 3: Custom Key Grouping
unordered_map<string, vector<string>> groups;
for (const auto& item : items) {
    string key = generateKey(item); // custom key generation
    groups[key].push_back(item);
}
```

```cpp
// Template 4: Hash Set for Sequence Problems
unordered_set<int> numSet(nums.begin(), nums.end());
for (int num : numSet) {
    if (numSet.find(num - 1) == numSet.end()) { // start of sequence
        int length = 1;
        while (numSet.find(num + length) != numSet.end()) {
            length++;
        }
        // process sequence
    }
}
```

### Common Edge Cases
- Empty arrays/strings
- Single element cases
- All elements identical
- Very large or very small numbers
- Special characters in strings (for string problems)

## Complexity Analysis Summary

### Time Complexity Patterns
- Brute force approaches: O(n²) for pair checking, O(n log n) for sorting
- Optimal hash approaches: O(n) for single pass, O(n*k) when key generation costs k
- Bucket sort optimization: O(n) when applicable

### Space Complexity Trade-offs
- Hash map solutions: O(n) space for O(1) lookup time
- In-place alternatives: O(1) space but worse time complexity
- Space-time trade-off almost always favors hash approach for this topic

## Key Insights & Lessons

### Strategic Insights
- Hash maps transform many O(n²) problems into O(n) solutions
- Key design is crucial - strings, coordinates, frequency arrays all work as keys
- One-pass is often possible and more elegant than two-pass approaches
- Starting sequences at natural beginning points avoids redundant work

### Technical Lessons
- `unordered_map` is the most versatile and frequently used container
- Reference usage (`const auto&`) prevents expensive copying
- Standard library functions (`sort`, `to_string`) simplify key generation
- Iterator patterns are essential for safe hash map access

### Mistake Patterns
- Initially overcomplicated simple problems (Q.242 with ASCII codes)
- Forgot to handle empty inputs properly
- Used expensive operations in loops (vector creation, unnecessary sorting)
- Poor variable naming and redundant variables (Q.347 first attempt)

## Cross-Topic Connections

### Foundation for Other Topics
- **Two Pointers**: Hash maps provide alternative approaches for sum problems
- **Sliding Window**: Frequency counting with hash maps will be essential
- **Trees**: Hash maps for parent-child relationships and path tracking
- **Graphs**: Hash maps for adjacency lists and visited tracking

### Building on Array Manipulation
- Prefix/suffix techniques (Q.238) bridge to dynamic programming
- Bucket sort concepts prepare for advanced sorting algorithms
- Index-based hash maps prepare for more complex data structure problems

## Progress Metrics

### Speed Improvements
- Early problems (Q.217): 56 minutes including learning
- Mid-period (Q.347): 46 minutes but first successful solo medium solve
- Later problems (Q.36): 53 minutes for complex multi-constraint problem
- Pattern recognition significantly improved - faster problem identification

### Success Rates
- First-attempt solve rate: 6/9 (67%) 
- Problems requiring hints: Q.1 (with Grok), Q.271 (implementation details)
- Problems requiring multiple attempts: Q.128 (conceptual insight needed)
- Strong improvement trajectory once hash map patterns mastered

### Performance Achievements
- Q.347: 4ms, beats 35% (could be improved with better algorithm choice)
- Q.1: 3ms, beats 70% 
- Memory efficiency: Generally good, beats 89-95% on several problems

## Next Steps
- **Immediate next topic**: Continue with Two Pointers (already completed) or Sliding Window
- **Prerequisite review needed**: Solid foundation established - ready for advanced topics
- **Specific goals**: 
  - Improve algorithm selection for optimal time complexity (heap vs bucket sort)
  - Reduce first-attempt solving time for medium problems
  - Master bitmask techniques introduced in Q.36 for space optimization