#!/usr/bin/env python3
import rbtracing
import maze
import sys
import wavefront

def main():
    mazeobj = maze.Maze()

    if len(sys.argv) > 1:
        print("Args: ", len(sys.argv))
        print("Loading maze from arg")
        mazeobj.load(sys.argv[1])

    else:
        print("Creating maze")
        mazeobj.create_random_maze(20,20)

    tracker = rbtracing.RecursiveBackTracker()

    start = (0,0)
    end = (4,4)
    
    tracker.solve(mazeobj, start, end)
    print(mazeobj.renderPath(tracker.path, start, end))
    print(tracker.path)

    solver = wavefront.WaveFrontPlanner(start,end,mazeobj)
    solver.weighGrid()
    print(mazeobj.renderPath(solver.returnPath(),start,end))
    print(solver.returnPath())

if __name__== "__main__":
    main()