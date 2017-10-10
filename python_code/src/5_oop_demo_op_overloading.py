class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)



pointA = Point(1,1)
pointB = Point(4,4)
print(pointA + pointB)
