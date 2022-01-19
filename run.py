import random
import argparse
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from common.genautomata import updateGrid
from automata.conway import conwayRules
from automata.darwin import darwinRules
import automata.religion as religion
from automata.religion import religionRules

def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_argument('--size', dest='N', required=False)
    parser.add_argument('--rand', dest='random', required=False)
    parser.add_argument('--type', dest='form', required=False)
    #parser.add_argument('--interval', dest='interval', required=False)
    args = parser.parse_args()

    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
    # flag to randomize initial grid, 1 for yes omit for no
    randomFlag = 0
    if args.random and int(args.random) == 1:
        randomFlag = 1
    # choose automata to form (default is conway)
    rules = conwayRules
    if args.form and args.form != 'conway':
        aType = args.form
        if(aType == 'darwin'):
            rules = darwinRules
        if(aType == 'religion'):
            rules = religionRules
    size = (N, N)
    updateInterval = 50
    if(randomFlag != 0):
        if(rules == darwinRules):
            grid = np.random.choice([0,1,2,3], N*N, p=[0.9, 0.07, .02, .01]).reshape(N, N)
        elif(rules == religionRules):
            grid = np.random.randint(0, 2, size=(N, N))
        else:
            grid = np.random.randint(0, 2, size=(N, N))
    else:
        grid = np.zeros(size, dtype=int)
    if(rules == darwinRules):
        minVal, maxVal = 0, 10
        cmap = mpl.cm.viridis
        norm = mpl.colors.Normalize(vmin=minVal, vmax=maxVal)
        fig, ax = plt.subplots()
        img = ax.imshow(grid, cmap=cmap, norm=norm, interpolation='nearest')
    elif(rules == religionRules):
        godRow = random.randrange(N)
        godCol = random.randrange(N)
        grid[godRow, godCol] = 10
        religion.god = (godRow, godCol)
        fig, ax = plt.subplots()
        img = ax.imshow(grid, interpolation='nearest')
    else:
        fig, ax = plt.subplots()
        img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, updateGrid, fargs=(img, grid, N, rules), frames = 100, interval=updateInterval, save_count=50)
    plt.show()

if __name__ == '__main__':
    main()