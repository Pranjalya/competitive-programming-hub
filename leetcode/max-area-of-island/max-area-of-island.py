class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.grid = grid
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if self.grid[i][j]:
                    ans = max(ans, self.getArea(i,j))
        return ans

    def getArea(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
            return 0
        if self.grid[i][j]:
            self.grid[i][j] = 0
            return self.getArea(i+1,j)+self.getArea(i,j+1)+self.getArea(i-1,j)+self.getArea(i,j-1)+1
        return 0
