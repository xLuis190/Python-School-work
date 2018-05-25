class SimpleRectangle:
    def __init__(self, length = 0, width = 0):
        self.l = length
        self.w = width;
    def getLength(self):
        return self.l
    
    def getWidth(self):
        return self.w;

    def __str__(self):
        return "The length is: {}\nThe width is: {}".format(self.getLength(),self.getWidth())

    def getArea(self):
        return self.getLength() * self.getWidth()

    def getPerimeter(self):
        return 2*(self.getLength() + self.getWidth())


R = SimpleRectangle(4,5)
print("Area: ", R.getArea())
print("Perimeter: ", R.getPerimeter())
print(R)
