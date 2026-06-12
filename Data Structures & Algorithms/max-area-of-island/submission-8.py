from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=((-1,0),(1,0),(0,-1),(0,1))
        max_square=0
        rows, cols=len(grid),len(grid[0]) 
        max_func = max

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    island_size=0
                    queue=deque([(i,j)])
                    grid[i][j]=0
                    # Define them locally right before the while loop starts
                    append_func = queue.append
                    popleft_func = queue.popleft

                    while queue:
                        island_size+=1
                        r,c=popleft_func()
                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                append_func((nr,nc))
                    max_square=max_func(max_square,island_size) 

        return max_square
        