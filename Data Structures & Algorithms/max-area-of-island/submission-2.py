from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions=((-1,0),(1,0),(0,-1),(0,1))
        max_square=0
        rows, cols=len(grid),len(grid[0]) 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    island_size=0
                    queue=deque([(i,j)])
                    grid[i][j]=0

                    while queue:
                        island_size+=1
                        r,c=queue.popleft()

                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue.append((nr,nc))

                    max_square=max(max_square,island_size) 

                        # if r>0 and grid[r-1][c]==1:
                        #     grid[r-1][c]=0
                        #     queue.append((r-1,c))
                        # if r<rows-1 and grid[r+1][c]==1:
                        #     grid[r+1][c]=0
                        #     queue.append((r-1,c))
                        # if c>0 and grid[r][c-1]==1:
                        #     grid[r][c-1]=0
                        #     queue.append((r,c+1))
                        # if r>0 and grid[r][c+1]==1:
                        #     grid[r][c+1]=0
                        #     queue.append((r,c))
                    
                    
        
        return max_square
        