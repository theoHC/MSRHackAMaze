import cell
class Maze:

    def __init__(self) :
        self.maze = [1][1]
        for row in self.maze:
            for element in row:
                element = Cell(True)
    
    def load(self,path):
        print("loading")
    
    def __str__(self):
        print("printing")
        row_index = 0
        for row in self.maze:
            row_index += 1
            if row_index % 2 == 1:
                print(" ", end="")
            for element in row:
                if element.isFree:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
                print("")
