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

                        if 0 <= r-1 and grid[r-1][c] == 1:
                            grid[r-1][c] = 0
                            queue.append((r-1,c))
                        if 0 <= c-1 and grid[r][c-1] == 1:
                            grid[r][c-1] = 0
                            queue.append((r,c-1))
                        if rows > r+1 and grid[r+1][c] == 1:
                            grid[r+1][c] = 0
                            queue.append((r+1,c))
                        if cols > c+1 and grid[r][c+1] == 1:
                            grid[r][c+1] = 0
                            queue.append((r,c+1))

                    max_square=max(max_square,island_size) 

        return max_square
        