class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self, y):
        super().__init__()
        self.y = self.x + y

b = B(5)
print(b.y)
