class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0]* columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        #first column sum
        for j in range(1,columns):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # first rows sum
        for i in range(1,rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # remaining sum
        for i in range(1,rows):
            for j in range(1,columns):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[rows-1][columns-1] # Last element is the minimum sum

        