# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


class Solution:
    def islandPerimeter(self, grid):
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (j > 0 and grid[i][j - 1] == 0) or j == 0:
                        cnt += 1

                    if (i > 0 and grid[i - 1][j] == 0) or i == 0:
                        cnt += 1

                    if (j < m - 1 and grid[i][j + 1] == 0) or j == m - 1:
                        cnt += 1

                    if (i < n - 1 and grid[i + 1][j] == 0) or i == n - 1:
                        cnt += 1
        return cnt
    

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        perimeter = 0
        
      
        for i in range(R):
            for j in range(C):
              
                if grid[i][j] == 1:
                    perimeter += 4
                    
                
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2

               
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter


from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            # If out of bounds or water, count as perimeter
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            # If already visited, don't count again
            if grid[i][j] == -1:
                return 0
            
            # Mark as visited
            grid[i][j] = -1
            
            # Explore all four directions
            return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        # Find the first land cell and start DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
        return 0


from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque()
        perimeter = 0
        
        # Find the first land cell and start BFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = -1  # Mark as visited
                    break
            if queue:
                break
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] == 0:
                    perimeter += 1
                elif grid[nx][ny] == 1:
                    queue.append((nx, ny))
                    grid[nx][ny] = -1  # Mark as visited
        
        return perimeter
