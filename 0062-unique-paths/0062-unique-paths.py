class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #robot can only move down and to the right
        #To find grid[m-1][n-1], it is unique paths to grid[m-2][n-1] + unique maths to grid[m-1][n-2]
        #So, we should know the path from above and the path from the left
        #Thus, top row and left column are the base cases of steps, starting at 1
        #Then, we can just work our way going down and across the rows each step down?
        #similar to the steps problem but in 2d

        grid = [[0] * n for i in range(m)] #m x n grid

        #Base cases
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        #space optimized, find min(m, n)
        #The value can rely on a saved past row/column and the current one. So the value in each slot starts at 1, then is past row/column slot + last slot in current row/column

        minimum = min(m, n)
        maximum = max(m, n)
        grid1 = [1] * minimum

        for i in range(1, maximum):
            for j in range(1, len(grid1)):
                grid1[j] = grid1[j - 1] + grid1[j]
        
        return grid1[-1]
