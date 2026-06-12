class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions=((-1,0),(1,0),(0,-1),(0,1))
        max_square=0
        rows, cols=len(grid),len(grid[0]) 

        def dfs(r,c):
            grid[r][c]=0
            current_isle_size=1
            for dr,dc in directions:
                nr, nc = r + dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    current_isle_size+=dfs(nr,nc)
            return current_isle_size
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    isle_size=dfs(i,j)
                    if max_square<isle_size: max_square=isle_size
        
        return max_square
        