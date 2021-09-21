from collections import deque
from maze import Maze
from tracer import Tracer
# import main
# BFS algorithm for Maze traversal
class BFS:
    def __init__(self, maze, start, destination):
        self.matrix = maze
        self.start = start
        self.dest = destination

    def BFSf(self):
        m = n = len(self.matrix)
        visited_blocks = [[False for _ in range(m)] for _ in range(n)]
        # initializing the possible ways from a co-ordinate
        adj_x = [-1, 0, 0, 1]
        adj_y = [0, -1, 1, 0]
        possibilities = len(adj_x)
        queue = deque()
        visiting_path = [(self.start.x, self.start.y)]  # storing the current path as tuple
        check_grid = Tracer(self.start, 0, visiting_path)
        queue.append(check_grid)
        cost = 0
        
        while queue:
            current_block = queue.popleft()     # deque from the queue and checking the possibble ways
            current_pos = current_block.pos  
            
            if current_pos.x == self.dest.x and current_pos.y == self.dest.y:
                return (current_block.cost, cost, current_block.path)
        
            if current_block not in visited_blocks:
                visited_blocks[current_pos.x][current_pos.y] = True
                cost = cost + 1
            cur_x = current_pos.x
            cur_y = current_pos.y
            for i in range(possibilities):
                if cur_x == len(self.matrix) - 1 and adj_x[i] == 1:
                    cur_x = current_pos.x
                    cur_y = current_pos.y + adj_y[i]
                else:
                    cur_x = current_pos.x + adj_x[i]
                    cur_y = current_pos.y + adj_y[i]
                
                if cur_x < m and cur_y < n and cur_x >= 0 and cur_y >= 0:
                    if self.matrix[cur_x][cur_y] == 1:
                        if not visited_blocks[cur_x][cur_y]:
                            my_path = current_block.path.copy() # copying the path traced till current
                            next_cell = Tracer(Maze(cur_x, cur_y), current_block.cost + 1, my_path)
                            my_path.append((cur_x, cur_y))
                            visited_blocks[cur_x][cur_y] = True
                            queue.append(next_cell)
        return -1