# Time Complexity: O(m * n)
# Space Complexity: O(n), not count the result space
# where m is the row number of grid, n is the column number of grid

class Solution:

    def possiblePaths(self, grid):

        ROWS, COLS = len(grid), len(grid[0])

        def initiateRow(rowIndex):
            row = [0] * (COLS + 1)
            for i in range(COLS - 1, -1, -1):
                if grid[rowIndex][i] == 0:
                    row[i] = 1
                else:
                    break
            return row

        row = initiateRow(ROWS - 1)
        for i in range(ROWS - 2, -1, -1):
            newRow = initiateRow(i)
            for j in range(COLS - 1, -1, -1):
                if grid[i][j] == 0:
                    newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]



print(Solution().possiblePaths(
[[0,0,0],[0,1,0],[0,0,0]]
))
print(Solution().possiblePaths(
[[0,1],[0,0]]
))
print(Solution().possiblePaths(
[[0,0,1,0],[0,0,0,0],[0,1,0,0]]
))
print(Solution().possiblePaths(
[[0,0,1,0],[0,0,0,0],[0,1,0,1]]
))
print(Solution().possiblePaths(
[[0,1,0,0],[0,0,0,0]]
))