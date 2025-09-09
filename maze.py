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

    def __str__(self):
        output = ""
        for row_index, row in enumerate(self.maze):
            row_index += 1
            if row_index % 2 == 1:
                output += " "
            for element in row:
                if element.isFree:
                    output += "* "
                else:
                    output += "# "
            if row_index < len(self.maze):
                output += "\n"
        return output
    

    def create_random_maze(self, row, col): 
        # This function creates a random maze that has a solution 
        
        mazeobj = Maze() 
        
        # Creating a maze in which all the cells are walls 
        for i in range(row): 
            mazeobj.maze.append([]) 
            for j in range(col): 
                new_cell = cell.Cell(False, i, j) 
                mazeobj.maze[i].append(new_cell) 
                
        # The current cell we are planning to free, the location of initial cell is random 
        curr_x = random.randint(0, row-1) 
        curr_y = random.randint(0, col-1) 
        curr_cell = (curr_x, curr_y) 
        mazeobj.maze[curr_x][curr_y].isFree = True 

        fron_cells, fron_num = [], 0 
        times = 0 
        max_times = row*col
        while times <= max_times: 
            nei_cells, nei_num = mazeobj.getAllWallNeighbors(curr_cell)
            for nei_cell in nei_cells: 
                if nei_cell not in fron_cells: 
                    fron_cells.append(nei_cell) 
                    fron_num += nei_num 

            if not fron_cells:
                break

            next_potential = random.choice(fron_cells) 

            # Search for the next cell that is surrounded by walls 
            #_, next_potential_nei = mazeobj.getAllWallNeighbors(next_potential) 
            times = 0 
            found = False
            while times < max_times: 
                _, wall_count = mazeobj.getAllWallNeighbors(next_potential) 
                nei_count = len(mazeobj.getAllNeighbors(next_potential))

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
            mazeobj.maze[curr_x][curr_y].isFree = True

            if curr_cell in fron_cells:
                fron_cells.remove(curr_cell)
        return mazeobj


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
        
        return Output

    def getNumFreeNeighbors(self, coords):
        return len(self.getAllFreeNeighbors(coords))
    

def main(): 
    new_maze = Maze().create_random_maze(20,20) 
    print(new_maze) 
    

if __name__ == "__main__": 
    main()
        
