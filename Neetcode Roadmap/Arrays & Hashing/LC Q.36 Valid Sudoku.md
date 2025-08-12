# LC Q.36 Valid Sudoku

2025.08.06.

Difficulty: #medium

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 22:32

End Time: 23:25

## My Approaches

### Basic Ideas
1. Brute Force?
- Create a function to check the repetition
- Create three loop to check the row, column, and sub-boxes

### Submission Code 1 (Solved)
~~~cpp
class Solution {
public:
    bool checkRepetition(vector<char>& cellGroup) {
        unordered_map<char, int> count;
        char dot = '.';
        for (char num : cellGroup) {
            if (num == dot) {
                continue;
            }
            count[num]++;
        }
        for (const auto& pair : count) {
            if (pair.second > 1) {
                return false;
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        // check the row
        for (vector<char> row : board) {
            bool rowCheck = checkRepetition(row);
            if (rowCheck == false) {
                return false;
            }
        }
        
        // check the column
        for (int i{0}; i < 9; ++i) {
            vector<char> col;
            for (vector<char>& row : board) {
                col.push_back(row[i]);
            }
            bool colCheck = checkRepetition(col);
            if (colCheck == false) {
                return false;
            }
        }

        // check the sub-boxes
        for (int j{0}; j < 9; ++j) {
            int rowNum{(j / 3) * 3};
            int colNum{(j % 3) * 3};
            vector<char> subx;
            for (int k{0}; k < 3; ++k) {
                subx.push_back(board[rowNum][colNum+k]);
                subx.push_back(board[rowNum+1][colNum+k]);
                subx.push_back(board[rowNum+2][colNum+k]);
            }
            bool subxCheck = checkRepetition(subx);
            if (subxCheck == false) {
                return false;
            }
        }
        return true;
    }
};
~~~

- Time complexity = O($n^2$) probably: 7ms, beats 36.28%
-  Space Complexity = O($n$)? beats 7.54%...
 
It is not a very good way to solve, but anyway, I did it as I planned.

### What I found out to code the approach
Not very much, it was mostly applying things that I already know.
One small thing was that to assign dot to char, I need to do '.', not "."...
And do NOT forget to put reference not to make expensive copy!!!

Some improvements that can be made advised by Claude are:
**Code Quality Issues**:
- Redundant comparisons: if (rowCheck == false) should be if (!rowCheck)
- Inconsistent naming: subx is unclear (maybe subBox?)
- Performance: Rebuilding column vectors is O(n²) when it could be O(n)
- Memory inefficiency: Passing vectors by value creates unnecessary copies (use vector<char>&)

**Style/Readability**:
- Verbose conditionals: Multiple if (check == false) return false patterns
- Mixed initialization styles: int i{0} vs standard int i = 0

## Solutions

### Solution 1 (Brute Force)
~~~cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[row][i] == '.') continue;
                if (seen.count(board[row][i])) return false;
                seen.insert(board[row][i]);
            }
        }

        for (int col = 0; col < 9; col++) {
            unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[i][col] == '.') continue;
                if (seen.count(board[i][col])) return false;
                seen.insert(board[i][col]);
            }
        }

        for (int square = 0; square < 9; square++) {
            unordered_set<char> seen;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }

        return true;
    }
};
~~~

Compared to my solution,
- row & column check:
  - I stored the whole vector to unordered map and then check the duplicates
  - this code simply check the vector itself by:
    - create unordered set named seen to store seen objects/cells
    - every iteration check if the cell is already stored in seen or not
- sub-box check:
  - Basically same logic as me, but better method for checking duplicates

Time Complexity: $O(n^2)$
Space Complexity: $O(n^2)$

### Solution 2 (One Pass Hash Set)
~~~cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows, cols;
        map<pair<int, int>, unordered_set<char>> squares;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                // Calculate which 3x3 box this cell belongs to
                pair<int, int> squareKey = {r / 3, c / 3};

                // Check if current digit violates ANY of the three Sudoku rules
                // 1. Row check / 2. Column check / 3. Square check
                if (rows[r].count(board[r][c]) || cols[c].count(board[r][c]) || squares[squareKey].count(board[r][c])) {
                    return false;
                }

                // record validated digits in all relevant sets
                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};
~~~

Damn, this is super elegant and clean solution...
Actually, one of the best approaches to the problem that I've ever seen...

Time Complexity: $O(n^2)$
Space Complexity: $O(n^2)$

### Solution 3 (Bitmask)
~~~cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // use integers as bit arrays: Each bit position represents whether digit 1-9 has been seen
        int rows[9] = {0};
        int cols[9] = {0};
        int squares[9] = {0};

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') continue;

                // convert character to bit position
                int val = board[r][c] - '1';

                // Check if the bit for this digit is already set in any constraint
                if ((rows[r] & (1 << val)) || (cols[c] & (1 << val)) ||
                    (squares[(r / 3) * 3 + (c / 3)] & (1 << val))) {        // & operation checks if that specific bit is already 1
                    return false;
                }

                // Set the bit for this digit in all relevant constraints
                rows[r] |= (1 << val);                              // |= performs bitwise OR assignment (turns the bit ON)
                cols[c] |= (1 << val);
                squares[(r / 3) * 3 + (c / 3)] |= (1 << val);
            }
        }
        return true;
    }
};
~~~

This is further improved version of solution 2.
Instead of storing whole arrays, it simplifies to bits, which is why this is called 'bitmask'.
This bitmask technique seems very useful, so I should memorize it... 

Time Complexity: $O(n^2)$
Space Complexity: $O(n)$

### Challenge Solution
If I get more confident with C++, read this part & try to learn its technique
(Brute Force with all complexities O(1))
~~~cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i=0; i<9; ++i) {
            vector<int> row(10,0), col(10,0);
            for (int j=0; j<9; ++j) {
                // row wise check
                if (board[i][j] != '.') {
                    if (++row[board[i][j]-'0']==2) return false;
                }
                // column wise check
                if (board[j][i] != '.') {
                    if (++col[board[j][i]-'0']==2) return false;
                }
            }
        }
         
        // in box check
        for (int i=0; i<9; i+=3) {
            for (int j=0; j<9; j+=3) {
                vector<int> box(10,0);
                for (int k=i; k<i+3; ++k) {
                    for (int l=j; l<j+3; ++l) {
                        if (board[k][l] == '.') continue;
                        if (++box[board[k][l]-'0']==2) return false;
                    }
                }
            }
        }
        return true;
    }
};
~~~