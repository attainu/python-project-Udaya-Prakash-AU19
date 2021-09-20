from maze import Maze
from tracer import Tracer
from bfs import BFS

if __name__ == '__main__':
    print("main start\n")
    matrix = [[1, 0, 0, 0],
              [1, 1, 0, 1],
              [0, 1, 0, 0],
              [1, 1, 1, 1]]
              
    start = Maze(0, 0)
    destination = Maze(3, 3)
    result = BFS(matrix, start, destination)
    steps = result.BFSf()
    if result != -1:
        print("Shortest path steps = ", steps)
    else:
        print("Path doesn't exist")