#!/usr/bin/env python3

import maze
import sys

def main():
    if sys.argv.len() > 1:
        mazeobj = maze()

        mazeobj.load(sys.argv[0])

        print(mazeobj)

if __name__== "main":
    main()