import cell
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
                
    def getAllFreeNeighbors(self,coords):
        Output = []

        for entry in getAllNeighbors(coords) :
            if(self.maze[coords[0]][coords[1]].isFree):
                Output.append(entry)
        
        return Output

    def getNumFreeNeighbors(self, coords):
        return len(getAllFreeNeighbors(coords))
        
