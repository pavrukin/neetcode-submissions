from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=((-1,0),(1,0),(0,-1),(0,1))
        max_square=0
        rows=len(grid)
        cols=len(grid[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    island_size=0
                    grid[i][j]=0
                    queue.append((i,j))                      
                    while queue:
                        island_size+=1
                        r,c=queue.popleft()
                        for dr in (-1,1):
                            nr=dr+r
                            if (0 <= nr) and (nr < rows) and (0 <= c) and (c < cols) and grid[nr][c] == 1:
                                grid[nr][c] = 0
                                queue.append((nr,c))

                        for dc in (-1,1):
                            nc=dc+c
                            if (0 <= r) and (r < rows) and (0 <= nc) and (nc < cols) and grid[r][nc] == 1:
                                grid[r][nc] = 0
                                queue.append((r,nc))
                        

                    max_square=max(max_square,island_size) 

        return max_square
        