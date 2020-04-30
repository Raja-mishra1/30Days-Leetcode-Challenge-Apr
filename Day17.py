class Solution:
    def dfs(self,grid,i,j):
        grid[i][j] = '0'
        for c,r in [i-1,j],[i+1,j],[i,j-1],[i,j+1]:
            if 0 <= c < len(grid) and 0 <= r < len(grid[0]) and grid[c][r] == '1':
                self.dfs(grid,c,r)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count  += 1
        return count