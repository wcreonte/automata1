import math
import random
from common.genautomata import neighborhoodScore

god = None

def distFromGod(cell):
    y = abs(god[0] - cell[0])
    x = abs(god[1] - cell[1])
    y2 = y**2
    x2 = x**2
    return int(round(math.sqrt(x2 + y2)))

def godScale(grid, dist):
    N = len(grid)
    if(dist >= 0 and dist <= N/20):
        return 5
    if(dist > N/20 and dist <= N/10):
        return 4
    if(dist > N/10 and dist <= N/5):
        return 3
    if(dist > N/5 and dist <= N/2):
        return 2
    if(dist > N/2):
        #missionary
        return random.choices([1, 5], weights=[99, 1])[0]



# main idea of this rule is one 'God' cell, behavior of others defined around it
def religionRules(grid, cell, neighbors):
    cellValue = grid[cell[0], cell[1]]
    #god cell
    if(cellValue >= 10):
        return cellValue + 1
    live, score = neighborhoodScore(grid, neighbors)
    dist = distFromGod(cell)
    religion = godScale(grid, dist)
    if(cellValue > 0):
        if(live < 2 or live > 3):
            if(score > 2):
                choices = [0, score]
                weights = [1, int(max(1, religion - 1))]
                return random.choices(choices, weights=weights)[0]
            else:
                if(live < 2):
                    if(religion == 5):
                        return random.choices([cellValue - 1, religion], weights = [1, 4])[0]
                    else:
                        return cellValue - 1
                elif(live > 3):
                    return random.choices([0, int(max(1, religion - 1))], weights=[4, 1])[0]
        elif(live == 2 or live == 3):
            if(religion >= 4):
                return random.choices([cellValue, int(min(5, cellValue + 1))])[0]
            else:
                return cellValue
    elif(cellValue == 0):
        if(live == 3 or religion == 5):
            return 1
        else:
            if(religion == 5):
                return random.choices([0, 1], weights=[9, 1])[0]
            else:
                return 0