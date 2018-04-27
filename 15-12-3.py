
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        print(self.y / self.x)


Point(4, 10).slope_from_origin()