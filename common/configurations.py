#places NxN block (of 1s) on specified grid where coords is the upper-left corner of the placed block
def block(grid, gridSize, coords, N):
    y = coords[0]
    x = coords[1]
    if(x < 0 or x > gridSize - 1 or y < 0 or y > gridSize - 1):
        return grid
    for i in range(N):
        for j in range(N):
            if(x + i  >= gridSize or y + j >= gridSize):
                break
            grid[x + i, y + j] = 1
    return grid

#places length N line (of 1s) on specified grid where coords is the startpoint part of line, which extends
#in direction based on dir input
def line(grid, gridSize, coords, N, dir):
    y = coords[0]
    x = coords[1]
    if(x < 0 or x > gridSize - 1 or y < 0 or y > gridSize - 1):
        return grid
    if(dir == 'left'):
        for i in range(N):
            if(x - i < 0):
                break
            grid[y, x-i] = 1
    if(dir == 'right'):
        for i in range(N):
            if(x + i >= gridSize):
                break
            grid[y, x+i] = 1
    if(dir == 'up'):
        for i in range(N):
            if(y - i < 0):
                break
            grid[y - i, x] = 1
    if(dir == 'down'):
        for i in range(N):
            if(y + i >= gridSize):
                break
            grid[y + i, x] = 1
    return grid

#places conway glider at coords on grid, where coords is the top-left corner of imaginary 3x3 block that glider sits in 
#(coords spot will be empty)
def glider(grid, gridSize, coords):
    y = coords[0]
    x = coords[1]
    if(x < 0 or x + 2 > gridSize - 1 or y < 0 or y + 2 > gridSize - 1):
        return grid
    grid[y, x + 1] = 1
    grid[y + 1, x + 2] = 1
    grid[y + 2, x] = 1
    grid[y + 2, x + 1] = 1
    grid[y + 2, x + 2] = 1
    return grid