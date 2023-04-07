class Rectangle:

    def __init__(self, x, y, a, b, color=[100, 100, 100]):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.b, :] = self.color
        return canvas


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side, :] = self.color
        return canvas
