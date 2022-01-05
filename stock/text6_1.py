class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def set_x(self, x) :
        self.x = x
    def set_y(self, y) :
        self.y = y
    def get(self) :
        return (self.x, self.y)
    def move(self, dx, dy) :
        self.x = self.x + dx
        self.y = self.y + dy
        return (self.x, self.y)
a = Point(3,3)
print(a.get())
# print(a.set_x(4))
# print(a.set_y(4))
print(a.get())
print(a.move(-2,-1))
print('total =', a.get())
