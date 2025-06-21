class Stack:
    def __init__(self):
        self.List = []
    
    def push(self, element):
        self.List.append(element)
        return self.List
    def pop(self):
        if len(self.List) != 0:
            return self.List.pop()
        else :
            print("Cannot")

Elist = Stack()
for i in range(5):
    Elist.push(i)
for i in range(5):
    print(Elist.pop())