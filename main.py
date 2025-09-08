#!/usr/bin/env python3

import maze
import sys

def main():
    print("Args: ", len(sys.argv))
    if len(sys.argv) > 1:
        print("Loading maze from arg")
        mazeobj = maze.Maze()

        mazeobj.load(sys.argv[0])

        print(mazeobj)

if __name__== "__main__":
    main()