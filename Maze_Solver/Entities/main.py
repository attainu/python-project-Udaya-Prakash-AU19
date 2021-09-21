from maze import Maze
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
    solution = result.BFSf()
    
    steps = solution[0]
    total_steps = solution[1]
    route = solution[2]

    if result != -1:
        print("Maze solved!!")
        print("Solved path:")
        m = n = len(matrix)
        sol = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(route)):
            sol_x = route[i][0]
            sol_y = route[i][1]
            sol[sol_x][sol_y] = 1

        for j in range(m):
            print(*sol[j])
        
        print("Shortest path steps = ", steps)
        print("Total visited steps = ", total_steps)

    else:
        print("Path doesn't exist")