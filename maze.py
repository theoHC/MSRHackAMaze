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
        print("printing")
        row_index = 0
        for row in self.maze:
            row_index += 1
            if row_index % 2 == 1:
                print(" ", end="")
            for element in row:
                if element.isFree:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
                print("")
