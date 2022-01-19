from common.genautomata import liveNeighbors

def conwayRules(grid, cell, neighbors):
    cellValue = grid[cell[0], cell[1]]
    live = liveNeighbors(grid, neighbors)
    if(cellValue == 1):
        if(live < 2 or live > 3):
            return 0
        elif(live == 2 or live == 3):
            return 1
    elif(cellValue == 0):
        if(live == 3):
            return 1
        else:
            return 0
