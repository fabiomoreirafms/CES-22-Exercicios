class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def collision_detection(self, r):
        distx = r.corner.x - self.corner.x
        disty = r.corner.y - self.corner.y
        X = distx >= -r.width and distx <= self.width
        Y = disty >= -self.height and disty <= r.height
        return X and Y


print(Rectangle(Point(0, 0), 100, 200).collision_detection(Rectangle(Point(-50, -200), 50, 50)))
