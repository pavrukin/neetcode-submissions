class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])
        island_counter=0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfc(r,c):
            grid[r][c] ="0"         
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]=="1":
                    dfc(nr,nc)
  
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfc(i,j)
                    island_counter+=1
        return island_counter
        