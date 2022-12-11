import collections

# Time Complexity: O(m * n)
# Space Complexity: max O(m * n), not count the result space
# where m, n is the size of grid

class Solution:

    def numberOfIsland(self, grid):

        queue = collections.deque()
        result = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    result += 1
                    grid[i][j] = '0'
                    queue.append([i, j])

                    while queue:
                        ro, co = queue.popleft()
                        if ro + 1 < rows and grid[ro + 1][co] == '1':
                            grid[ro + 1][co] = '0'
                            queue.append([ro + 1, co])
                        if ro - 1 >= 0 and grid[ro - 1][co] == '1':
                            grid[ro - 1][co] = '0'
                            queue.append([ro - 1, co])
                        if co + 1 < cols and grid[ro][co + 1] == '1':
                            grid[ro][co + 1] = '0'
                            queue.append([ro, co + 1])
                        if co - 1 >= 0 and grid[ro][co - 1] == '1':
                            grid[ro][co - 1] = '0'
                            queue.append([ro, co - 1])
        return result


print(Solution().numberOfIsland(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
))
print(Solution().numberOfIsland(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
))
print(Solution().numberOfIsland(
    [
        ["1", "1", "0", "0", "1"],
        ["1", "0", "0", "1", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "1", "0", "1", "1"]
    ]
))
print(Solution().numberOfIsland(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "1", "1"]
    ]
))
