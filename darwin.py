from common.genautomata import neighborhoodScore
from common.configurations import block, line, glider


def darwinRules(grid, cell, neighbors):
    live, score = neighborhoodScore(grid, neighbors)
    cellValue = grid[cell[0], cell[1]]
    if(cellValue == 0):
        if(live == 3):
            return 1
        else:
            return 0
    else:
        if(live < 2):
            if(cellValue < score):
                return 0
            if(cellValue >= score):
                return cellValue - 1
        elif(live > 3):
            if(cellValue < score):
                return max(0, cellValue - 2)
            elif(cellValue >= score):
                return cellValue
        elif(live == 2 or live == 3):
            if(abs(score - cellValue) < 3):
                return min(10, cellValue + 1)
            if(abs(score - cellValue) >= 3):
                return cellValue - int(round(abs(score - cellValue) / 2))


