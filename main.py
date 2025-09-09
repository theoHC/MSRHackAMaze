#!/usr/bin/env python3
import rbtracing
import maze
import sys
import wavefront

def main():
    mazeobj = maze.Maze()

    #Generate a maze if we provide no arguments, otherwise use the provided file
    if len(sys.argv) > 1:
        print("Args: ", len(sys.argv))
        print("Loading maze from arg")
        mazeobj.load(sys.argv[1])

    else:
        print("Creating maze")
        mazeobj.create_random_maze(20,20)

    #create a recursive backtracker and use it to solve our maze, printing its output
    tracker = rbtracing.RecursiveBackTracker()

    start , end = mazeobj.getRandomStartEnd()
    
    tracker.solve(mazeobj, start, end)
    print(mazeobj.renderPath(tracker.path, start, end))
    print(tracker.path)

    #create a wavefront solver and do likewise
    solver = wavefront.WaveFrontPlanner(start,end,mazeobj)
    solver.weighGrid()
    print(mazeobj.renderPath(solver.returnPath(),start,end))
    print(solver.returnPath())

if __name__== "__main__":
    main()