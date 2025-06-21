class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.r = radius
    def area_calc(self):
        A = self.r ** 2 * self.pi
        return A
    def peri_calc(self):
        P = self.r * self.pi * 2
        return P


C = Circle(5)
print(C.area_calc(), C.peri_calc())