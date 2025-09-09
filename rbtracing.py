import maze

class RecursiveBackTracker:
    def __init__(self):
        self.path = []
        self.visited = []
    
    #the beauty of recursive backtracking: one recusive function.
    def solve(self, problem, start, end):
        if(start == end):
            self.path.append(start)
            return True
        
        self.visited.append(start)

        for coords in problem.getAllFreeNeighbors(start)[0]:
            if(not coords in self.visited):
                if(self.solve(problem, coords, end)):
                    self.path.append(start)
                    return True

        return False