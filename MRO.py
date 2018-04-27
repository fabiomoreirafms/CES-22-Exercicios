class Polygon:

    def area(self):
        print("O cálculo pode ser complexo")

class RegularPolygon:
    geometric_type = "Regular Polygon"

    def __init__(self,side=0):
        self.side = side

    def area(self):
        print("Qual o tipo de poligono?")


class retangulo(Polygon):
    geometric_type = "Retângulo"

    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        print ("Area {0}".format(self.side1*self.side2))


class quadrado(RegularPolygon, retangulo):

    def __init__(self,side):
        super().__init__(side)

    def area(self):
        print("Area {0}".format(self.side*self.side))

A = RegularPolygon(2)
B = retangulo(2,3)
C = quadrado (4)

print("{0}".format(A.side))
print("{0}".format(A.geometric_type))
A.area()

print("{0} {1}".format(B.side1,B.side2))
print("{0}".format(B.geometric_type))
B.area()

print("{0}".format(C.side))
print("{0}".format(C.geometric_type))
C.area()