class Cell:

    def __init__(self,isFree,x,y):
        self.isFree = isFree
        self.prop = "" #will be set as start or end.
        self.x = x
        self.y = y