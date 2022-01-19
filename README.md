# Automata1

Visualizing well-known automata as well as experimenting with creating new automata around various mathematical and social concepts

## Running the visualizations

To run the visualizations, which are done through matplotlib animations, run 'run.py' file from the commandline with desired arguments

```bash
python3 .../repository_location/run.py --type conway --rand 1
```

## Arguments

Listed here are the possible flags to be added as command line arguments, what they do, and the possible values for the flags

#### -size
##### Provides the size for the generated NxN grid (default is N = 100)
Any number can be added here - note that low numbers will likely result in a short-lived or uninteresting animations, whereas large grids can incur performance issues.

#### --type
##### Notes which automata to be visualized
conway\n
religion\n
darwin

#### --rand
##### Tells whether to randomly populate the starting grid of the automata. Note that if omitted (or set to 0), there will be nothing to animate unless you have manually added pixels to the grid. Usually this is done to observe specific starting orientations or note the behavior of various configurations.
1\n
0

