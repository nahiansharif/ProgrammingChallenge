# https://leetcode.com/problems/game-of-life/ 


# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

class Solution(object):
    def gameOfLife(self, board):
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def count_live_neighbors(r, c):
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        count += 1
            return count

        for r in range(m):
            for c in range(n):
                live_neighbors = count_live_neighbors(r, c)

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
                    
class Solution:
    def gameOfLife(self, b):
        """
        Do not return anything, modify board in-place instead.
        
        apply by using:
            under-population: < 2
            live to next generation: 2 or 3 
            over-population: > 3
            reproduction: == 3
        
        simultaneously: shoud not use DFS/BFS
            
        \|/
        - -
        /|\
        """
        # all new 0's denotes as -1, (1 ==> 0)
        # all new 1's denotes as 2   (0 ==> 1)
        m, n = len(b), len(b[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for i in range(m):
            for j in range(n):
                livecount = 0
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    if 0 <= nr < m and 0 <= nc < n and abs(b[nr][nc]) == 1: # originally 1's
                        livecount += 1
                if b[i][j] == 1:
                    if livecount < 2 or livecount > 3:   
                        b[i][j] = -1
                else:
                    if livecount == 3:  
                        b[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if b[i][j] == 2:    b[i][j] = 1
                elif b[i][j] == -1: b[i][j] = 0
                
from collections import Counter               
def gameOfLifeInfinite(self, live):
    ctr = Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}
    
    
def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live)
            
class Solution(object):
    def gameOfLife(self, board):
        new = [row[::] for row in board]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                c_live = 0
                for d in directions:
                    x = i+d[0]
                    y = j+d[1]
                    if 0<=x<len(board) and 0<= y< len(board[0]) and new[x][y]:
                        c_live +=1
                if new[i][j]:
                    if c_live !=2 and c_live !=3:
                        board[i][j]=0
                else:
                    if c_live ==3:
                        board[i][j]=1