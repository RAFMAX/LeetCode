class Shape():
    def __init__(self, main, secondary=None):
        self.main = int(main)
        if secondary != None :
            self.secondary = int(secondary)
    def area(self):
        pass
    def peri(self):
        pass
class Square(Shape):
    def __init__(self, main):
        super().__init__(main)
    def area(self):
        return(self.main * self.main)
    def peri(self):
        return(self.main * 4)
class Circle(Shape):
    def __init__(self, main):
        super().__init__(main)
    def peri(self):
        return(self.main * 2 * 3.14)
    def area(self):
        return(self.main**2 * 3.14)
class Rectangle(Shape):
    def __init__(self, main, secondary):
        super().__init__(main, secondary)
    def area(self):
        return(self.main * self.secondary)
    def peri(self):
        return(self.main * 2 + self.secondary * 2)

R = Circle(6)

print(f"{R.peri()}, {R.area()}")

R = Rectangle(6, 5)

print(f"{R.peri()}, {R.area()}")

R = Square(6)

print(f"{R.peri()}, {R.area()}")
