class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])
        island_counter=0

        def dfc(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0":
                return
            
            grid[r][c]="0"

            dfc(r-1,c)
            dfc(r+1,c)
            dfc(r,c-1)
            dfc(r,c+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    dfc(i,j)
                    island_counter+=1
        return island_counter
        