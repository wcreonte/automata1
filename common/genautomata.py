from itertools import product

def getNeighbors(N, cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < N for n in c):
            yield c
    
def neighborValues(grid, neighbors):
    values = []
    for n in neighbors:
        y = n[0]
        x = n[1]
        values.append(grid[y, x])
    return values

def liveNeighbors(grid, neighbors):
    liveNeighborCount = 0
    for n in neighbors:
        if(grid[n[0], n[1]] >= 1):
            liveNeighborCount += 1
    return liveNeighborCount

# TODO - definitely matters if round up or down, look into this 
def neighborhoodScore(grid, neighbors):
    live = liveNeighbors(grid, neighbors)
    vals = neighborValues(grid, neighbors)
    score = 0
    if(live == 0):
        return 0, 0
    for v in vals:
        if(v >= 10):
            continue
        else:
            score += v
    score = int(round(score / live))
    return live, score

def applyRules(grid, N, rules):
    nextGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            neighbors = list(getNeighbors(N, (i, j)))
            nextGrid[i, j] = rules(grid, (i, j), neighbors)
    return nextGrid

#no idea why but it needs the gen input
#img is the animation, grid is the starting grid, N is size of grid, rules is rules to be applied to create automata
def updateGrid(gen, img, grid, N, rules):
    nextGrid = applyRules(grid, N, rules)
    img.set_data(nextGrid)
    grid[:] = nextGrid[:]
    return img