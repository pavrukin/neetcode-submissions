# from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=((-1,0),(1,0),(0,-1),(0,1))
        max_square=0
        rows, cols=len(grid),len(grid[0]) 
        max_func = max

        queue = [None] * (rows * cols)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    island_size=0
                    head=0
                    tail=0
                    grid[i][j]=0

                    queue[tail] = (i, j)
                    tail+=1


                    while head<tail:
                        island_size+=1

                        r, c = queue[head]
                        head += 1

                        for dr,dc in directions:
                            nr,nc=dr+r, dc+c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                queue[tail]= (nr, nc)
                                tail+=1
                                
                    max_square=max_func(max_square,island_size) 

        return max_square
        