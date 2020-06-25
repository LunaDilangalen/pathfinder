from random import randint, seed
from models import grid

seed(69)

# Creates a grid object with random walls
# using x and y as dimension parameters
# Returns a grid object
def createGrid(x, y):
    # initialize grid
    outputGrid = grid.Grid(x, y)

    # initialize a random list of walls
    # so as to not fill the whole grid with walls
    # walls list must have length = (xy)/2
    N = int((x*y)/8) 
    randomWalls = [0]*N
    # print(len(randomWalls))

    for i in range(N):
        # change the initial value to a tuple with random (x,y)
        # such that it is within the dimensions of the grid
        random_x = randint(0, x-1)
        random_y = randint(0, y-1)
        while((random_x, random_y) in randomWalls):
            random_x = randint(0, x-1)
            random_y = randint(0, y-1)
        randomWalls[i] = (random_x, random_y)
    # print(randomWalls)
    outputGrid.walls = randomWalls

    return outputGrid
def drawGrid(grid):
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.passable((x,y)):
                print('- ',end='')
            elif not grid.passable((x,y)):
                print('# ',end='')
        print('')

def reconstructPath(cameFrom, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    path.reverse()
    return path