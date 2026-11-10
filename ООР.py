import maltplotlib.pyplot as pll


def add(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    return (x,y)

v1 = (10, 5)
v2 = (3, 15)
v = v1 + v2
print(v)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def display_add(self, other):
        res = self + other
        x1 = [0, self.x]
        y1 = [0, self.y]
        x2 = [0, other.x]
        y2 = [0, other.y]
        rx = [0, res.x]
        ry = [0, res.y]

        plt.plat()
        plt.show()
    def __str__(self):
        return f'V({self.x}, {self.y})'

v1 = Vector(10, 5)
v2 = Vector(3, 15)
v3 = Vector(2, 4)

print(v1)
print(v2 + v1 + v3)
v1.display_add(v2)

"""S O L I D"""

