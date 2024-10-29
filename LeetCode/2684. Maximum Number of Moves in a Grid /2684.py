class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) #m: number of rows, n: number of columns
        dp = [[0] * n for _ in range(m)]
        
        found = False # can't move to the next column

        for j in range (1, n): #first column values = 0
            found = True
            for i in range (m):
                if i > 0 and grid[i][j] > grid[i-1][j-1] and dp[i-1][j-1] == j-1:
                    dp[i][j] = j
                    found = False
                    continue
                if grid[i][j] > grid[i][j-1] and dp[i][j-1] == j-1:
                    dp[i][j] = j
                    found = False
                    continue
                if i < m-1 and grid[i][j] > grid[i+1][j-1] and dp[i+1][j-1] == j-1:
                    dp[i][j] = j          
                    found = False
                    continue
            if found is True:
                break
        return max(max(row) for row in dp)
