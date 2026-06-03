# Two Pointer
## What it is
Two Pointer = technique that uses two or more pointers traversing the data structure
- Kinda broad topic, so no singular way to implement it
- Generally, a Two Pointer has such characteristics:
  - Two moving pointers, regardless of directions, moving independent/dependently
  - A function utilizing the entries referenced by two pointers
  - Easy way of deciding which ointer to move
  - Way to process the array when pointers are moved

## Classification
### Same Direction
How Two Pointer is used (e.g. Remove Duplicates):
- Compare the value of the fast pointer to its previous entry
- Then see if they match.

General Moving Condition:
- If the previous check match, only the fast pointer moves
- Otherwise, the slow pointer moves, perform the process of setting the value at the slow pointer to the value at the fast pointer
- Then the fast pointer moves

### Opposite Direction
How Two Pointer is used (e.g. Two Sum Sorted):
- Compare the sum of the entries to the desired amount

General Moving Condition:
- If the sum is greater, we move the larger pointer
- If the sum is equal, we find our answer and we stop the program

### Two Pointers VS Sliding Window
How Two Pointer is used (e.g. Longest Substring without Repeating Characters):
- Similar to same directions problems
  - Performs on the entire interval between the two pointers
- Usually keep track of the cumulative result of the window
- each time we insert/remove an item from the window, we simply update the window according to the changes

General Moving Condition:
- Keep track of the number of characters that appear in the window
- Move the later pointer, inserting the item into the set, until there is a duplicate
- Keep track of the largest size each time for the answer

### Non-Array Applications
Two pointer can be done on other structures, like linked list, as long as they are iterable.

## Why Two Pointers?
- often offers a more efficient solution than Brute Force