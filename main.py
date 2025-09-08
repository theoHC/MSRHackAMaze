#!/usr/bin/env python3
import rbtracing
import maze
import sys

def main():
    print("Args: ", len(sys.argv))
    if len(sys.argv) > 1:
        print("Loading maze from arg")
        mazeobj = maze.Maze()

        mazeobj.load(sys.argv[1])

        tracker = rbtracing.RecursiveBackTracker()

        start = (0,0)
        end = (4,4)
        
        tracker.solve(mazeobj, start, end)

        print(mazeobj.renderPath(tracker.path, start, end))
        print(tracker.path)

if __name__== "__main__":
    main()