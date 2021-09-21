# Steps to create a Maze Solver:

a) Create classes for separate entities

    `class Maze` - initializes co-ordinates of the maze
    
    `class Tracer` - stores the current co-ordinate and the cost of getting to that co-ordinate
    
    `class BFS` - BFS alorithem for maze traversal and finding the shortest path
    
    `class main` - here we start by calling the classes and functions and perform the actual operation

b) In Maze Solver, We need to traverse the path from source to destination.
So we have to create store the starting and ending positions in the form of co-ordinates. For that purpose, we have taken a `class Maze` and storing the row as 'x' and column as 'y'.

c) We need to keep track of the path we trace and the cost of getting into that path.
Hence we have taken another `class Tracer`, then the entire Maze is taken in a variable called 'pos' and the cost of getting to that position as 'cost'.

d) The actual maze traversal is performed in `class BFS`, we pass the arguments Matrix, start and destination as arguments to initialise the class. We call the `BFSf` function inside the BFS class which performs maze traversal.

Inside BFSf, we perform the actual Breadth First Search alorithem.

1) We append the current position inside a queue or deque.

2) If the current position == destination, then we will return the number of steps taken to reach the destination or the entire path to get to the destination itself, depending upon our need.

3) If the current position != destination, then mark it as 'visited' and then we will check the possible ways using 'for loop'.

4) If the path is available, we will append it into the queue and continue current iteration and finish it.

5) After the current path is completely checked for next position, we will return to the 'while loop'. Since the queue is not empty, we will continue to perform the above operation until we reach the destination.

6) If we don't get the destination throuhout the operation, we will return -1.