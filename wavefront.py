import maze

class WaveFrontPlanner:
    def __init__(self,start,goal,maze):
        self.start = start
        self.goal = goal
        self.maze = maze.maze
        self.problem = maze
        self.rows = len(self.maze)
        self.columns = len(self.maze[0])
        self.visited = []
        self.weight_grid = []

    def findValidNeighbours(self,x,y):
        '''Function to find all valid neighbours(neighbours which are not out of bound and not obstacles)'''
        neighbours = []
        possible_dirs = []
        if(x%2 == 0):
            possible_dirs = [(-1, 0),(-1, +1),(0, -1),(0, +1),(+1, 0),(+1, +1)]
        else :
            possible_dirs = [(0, -1),(0, +1),(+1, 0),(-1, 0),(-1,-1),(+1,-1)]

        for d_x,d_y in possible_dirs:
            if(x+d_x >= 0 and x+d_x < self.rows) and (y+d_y >= 0 and y+d_y < self.columns):
                if(self.maze[x+d_x][y+d_y].isFree):
                    neighbours.append((x+d_x,y+d_y))

        return neighbours
        
    def weighGrid(self):
        '''Solver for Wavefront Planner.'''
        weight_grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(-1)
            weight_grid.append(row)

        goal_x,goal_y = self.goal
        self.visited.append((goal_x,goal_y))

        weight_grid[goal_x][goal_y] = 0 
        while self.visited:
            x , y = self.visited.pop(0)
            current_weight = weight_grid[x][y]
            neighbours = self.findValidNeighbours(x,y)
            for coord in neighbours:
                x_n, y_n = coord[0], coord[1]
                if(weight_grid[x_n][y_n] == -1):
                    weight_grid[x_n][y_n] = current_weight + 1
                    self.visited.append((x_n,y_n))

        self.weight_grid = weight_grid

    def returnPath(self):
        '''Returns the path for the Wavefront Planner'''
        start_x, start_y = self.start
        path = []
        (cur_x ,cur_y) = self.start
        while (cur_x,cur_y) != self.goal:
            path.append((cur_x,cur_y))
            neighbour = self.findValidNeighbours(cur_x,cur_y)

            least_neighbour = neighbour[0]
            min_weight = self.weight_grid[least_neighbour[0]][least_neighbour[1]]

            for coord in neighbour:
                x_n, y_n = coord[0], coord[1]
                if self.weight_grid[x_n][y_n] < min_weight:
                    min_weight = self.weight_grid[x_n][y_n]
                    least_neighbour = (x_n,y_n)

            cur_x,cur_y = least_neighbour
        path.append(self.goal)
        return path
            

        



        
        


