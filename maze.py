import cell
import random

class Maze:

    def __init__(self) :
        self.maze = []
        self.cell = ""

    def load(self,path):
        with open(path) as f :
            for row_id,line in enumerate(f):
                row = []
                contents = line.strip().split()
                for col_id,symbol in enumerate(contents):
                    if(symbol == "*"):
                        row.append(cell.Cell(1,row_id,col_id))
                    if(symbol == "#"):
                        row.append(cell.Cell(0,row_id,col_id))
                self.maze.append(row)

    def renderPath(self, path=None, start=None, end=None):
        output = ""
        for row_index, row in enumerate(self.maze):
            row_index += 1
            if row_index % 2 == 1:
                output += " "
            for element in row:
                if element.isFree:
                    if((element.x, element.y) == start): output += "S "
                    elif((element.x, element.y) == end): output += "E "
                    elif((element.x, element.y) in path): output += "P "
                    else : output += "* "
                else:
                    if((element.x, element.y) in path): output += "! "
                    else : output += "# "
            if row_index < len(self.maze):
                output += "\n"
        return output

    def __str__(self):
        return self.renderPath(path=[])
    

    def create_random_maze(self, row=10, col=10): 
        # This function creates a random maze that has a solution 
                
        # Creating a maze in which all the cells are walls 
        for i in range(row): 
            self.maze.append([]) 
            for j in range(col): 
                new_cell = cell.Cell(False, i, j) 
                self.maze[i].append(new_cell) 
                
        # The current cell we are planning to free, the location of initial cell is random 
        curr_x = random.randint(0, row-1) 
        curr_y = random.randint(0, col-1) 
        curr_cell = (curr_x, curr_y) 
        self.maze[curr_x][curr_y].isFree = True 

        fron_cells, fron_num = [], 0 
        times = 0 
        max_times = row*col
        while times <= max_times: 
            nei_cells, nei_num = self.getAllWallNeighbors(curr_cell)
            for nei_cell in nei_cells: 
                if nei_cell not in fron_cells: 
                    fron_cells.append(nei_cell) 
                    fron_num += nei_num 

            if not fron_cells:
                break

            next_potential = random.choice(fron_cells) 

            # Search for the next cell that is surrounded by walls 
            #_, next_potential_nei = self.getAllWallNeighbors(next_potential) 
            times = 0 
            found = False
            while times < max_times: 
                _, wall_count = self.getAllWallNeighbors(next_potential) 
                nei_count = len(self.getAllNeighbors(next_potential))

                free_count = nei_count - wall_count
                if free_count == 1:
                    found = True
                    break
                times += 1
                next_potential = random.choice(fron_cells)

            if not found:
                break

            curr_cell = next_potential 
            curr_x, curr_y = curr_cell 
            self.maze[curr_x][curr_y].isFree = True

            if curr_cell in fron_cells:
                fron_cells.remove(curr_cell)
        #return self.maze

    #helper function to get all hexagonally adjacent cells
    def getAllNeighbors(self,coords):
        row = coords[0]
        col = coords[1]

        ############ begin citation [1] ############
        rows, cols = len(self.maze), len(self.maze[0])
        # Neighbor offsets differ depending on row parity
        if row % 2 != 0:  # even row
            directions = [(-1, 0), (-1, -1),
                        (0, -1), (0, 1),
                        (1, 0), (1, -1)]
        else:  # odd row
            directions = [(-1, 0), (-1, 1),
                        (0, -1), (0, 1),
                        (1, 0), (1, 1)]
        
        neighbors = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                neighbors.append((r, c))
        
        return neighbors
    ############ end citation [1] ############
                
    #bonus helper functions to filter for wall or free neighbors, since that's what we generally care about.
    def getAllWallNeighbors(self,coords):
        Output = [] 
        for (r,c) in self.getAllNeighbors(coords) :
            if not (self.maze[r][c].isFree): 
                Output.append((r,c))
        return Output, len(Output)
    
    
    def getAllFreeNeighbors(self,coords):
        Output = []

        for entry in self.getAllNeighbors(coords) :
            if(self.maze[coords[0]][coords[1]].isFree):
                Output.append(entry)
        
        return Output, len(Output)

    
#special main to test maze generation
def main(): 
    new_maze = Maze()
    new_maze.create_random_maze(20,20) 
    print(new_maze) 
    

if __name__ == "__main__": 
    main()
        
