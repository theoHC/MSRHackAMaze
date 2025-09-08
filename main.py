#!/usr/bin/env python3

import maze
import sys
import rbtracing
import wavefront

def main():
    print("Args: ", len(sys.argv))
    if len(sys.argv) > 1:
        print("Loading maze from arg")
        mazeobj = maze.Maze()

        mazeobj.load(sys.argv[1])

        print(mazeobj)
        solver = wavefront.WaveFrontPlanner((0,0),(1,4),mazeobj)
        solver.weighGrid()
        print(solver.returnPath())

if __name__== "__main__":
    main()