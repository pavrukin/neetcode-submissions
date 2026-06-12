from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # directions=((-1,0),(1,0),(0,-1),(0,1))
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
                        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                            if (0 <= dr+r) and (dr+r < rows) and (0 <= dc+c) and (dc+c < cols) and grid[dr+r][dc+c] == 1:
                                        grid[dr+r][dc+c] = 0
                                        queue.append((dr+r,dc+c))
                    max_square=max(max_square,island_size) 

        return max_square
        