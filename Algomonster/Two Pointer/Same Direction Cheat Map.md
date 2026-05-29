# Same Direction Cheat Map

## General Movement of Two Pointers
- usually scan left to right
- different jobs for each pointer
  - one reads the next value from the original input
  - one marks where the next kept value should go

## When to Apply
- Rewrite an array in-place
- Remove/Compress elements without extra memory
- Keep only values satisfying some condition
- Maintain a fixed gap between two forward-moving pointers

## Core Invariant
Invariant = usually the prefix that is already processed

Typical Invariant Example:
> Everything before write pointer is already in the correct final form

Note that:
- pointers are not searching from both sides
- they build answers progressively as moving through the input

## Subtypes
### 1. Compaction / Overwrite
Example: Exercise 1, 3

- Slow marks next output position
- Fast scans input
- When current must be kept, copy it forward & advance the slow

### 2. Relative Speed
Example: Exercise 2

- Both move forward, but fast moves twice as fast
- Invariant = their distance & how much of structure each pointer has consumed

### 3. Fixed Gap
Example: Exercise 4

- Both moves forward while preserves a gap
- Invariant = distance between pointers that first established at the start of algorithm

## Changes across Problems
Invariant changes slightly while the main family character -moving in the same direciton- remains.
- Array compaction: invariant = prefix being correct
- Fast/Slow Midpoint: invariant = relative speed
- Fixed-Gap: invariant = distance between pointers

Therefore, the unifying idea of this family is:
> the structure to the left of the pointers already has a known meaning

Which mean that we need to always ask a following question:
> What does the region before the slow pointer mean right now?

## Common Mistakes
- Update write pointer before copying the current
- Forget exactly what region is already valid
- Lose track of whether invariant is about a prefix, gap, or relative speed