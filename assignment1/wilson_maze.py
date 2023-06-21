import numpy as np
import random

def w_generate_maze(width, height):
    visited = []
    # Initialize the maze grid as all blocked
    maze = np.zeros((height, width), dtype=np.int8)

    # Define the directions we can move in the maze
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Define a function to check if a given cell is in the maze
    def in_maze(x, y):
        return 0 <= x < width and 0 <= y < height

    # Define a function to choose a random starting cell
    def choose_start():
        return (random.randint(0, width-1), random.randint(0, height-1))

    # Choose a random starting cell and mark it as visited
    start = choose_start()
    visited.append(start) 
    prob = random.uniform(0, 1)
    if (prob > 0.3): maze[start[1], start[0]] = 1

    # Initialize a list of unvisited cells
    unvisited = [(x, y) for x in range(width) for y in range(height) if (x, y) not in visited]

    # Define a function to choose a random unvisited cell
    def choose_unvisited():
        return random.choice(unvisited)

    # Define a function to walk a path from a given cell until we hit a visited cell
    def walk_path(x, y):
        path = []
        while in_maze(x, y) and (x, y) not in visited: 
            path.append((x, y))
            x += random.choice(directions)[0]
            y += random.choice(directions)[1]
        return path

    # Generate the maze using Wilson's algorithm
    while unvisited:
        # Choose a random unvisited cell to start a new path from
        start = choose_unvisited()
        # Walk a path until we hit a visited cell
        path = walk_path(start[0], start[1])
        # If the end of the path is in the maze, add it to the maze
        if in_maze(path[-1][0], path[-1][1]):
            x = path[-1][0]
            y = path[-1][1]
            prob = random.uniform(0, 1)
            if (prob > 0.3): maze[y, x] = 1
            visited.append((x, y))
            unvisited.remove((x, y)) 

    return maze

w_generate_maze(15, 15)