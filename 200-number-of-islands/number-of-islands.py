class Solution:
    def dfs(self, i,  j, grid,vis, n , m):
        if i<0 or j<0 or i>=n or j>=m or vis[i][j] or grid[i][j]!='1':
            return

        vis[i][j]= True
        self.dfs(i,j-1,grid,vis,n,m)
        self.dfs(i,j+1,grid,vis,n,m)
        self.dfs(i-1,j,grid,vis,n,m)
        self.dfs(i+1,j,grid,vis,n,m)

    def numIslands(self, grid: List[List[str]]) -> int:
        island =0
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)] 
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == '1' and not vis[i][j]:
                    self.dfs(i,j,grid,vis,n,m)
                    island+=1
        return island
