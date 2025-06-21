class Calculator:
    def __init__(self, N1, N2): 
        self.N1 = int(N1)
        self.N2 = int(N2)
    def add(self):
        return self.N1 + self.N2
    def sub(self):
        return self.N1 - self.N2
    def div(self):
        return self.N1 / self.N2
    def mul(self):
        return self.N1 * self.N2
    
N = Calculator(5, 6)
print(f"{N.add()}, {N.sub()}, {N.mul()}, {N.div()}")