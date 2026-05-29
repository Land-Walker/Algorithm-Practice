This is a doc where I jot down whatever I 'discover' tips to solve binary search questions easier.

- Binary search Qs are often just finding a suitable feasible() function to satisfy Q’s constraints
- How should we formulate feasible() function?
  - Must be comparison (bigger than, smaller than, etc)
  - This is because binary search is basically deletion of either right or left side to find the very first target in sorted array.
  - Note that left and right must be modified for different Qs so that overflow should not be happened
fd