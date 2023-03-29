import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, a, b, color = 'black'):
        self.a = a
        self.b = b
        self.color = color

    def make(self, imagepath):
        """
        Make the canvas and save it in the imagepath
        """
        canvas = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        if self.color == 'white':
            canvas[:] = [255, 255, 255]

        img = Image.fromarray(canvas, 'RGB')
        img.save(imagepath)


class Rectangle:

    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self, canvas):
        pass


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass


sq = Square(2, 8, 3, 1)
print(sq.x, sq.y)

cnv = Canvas(3, 4)
cnv.make('cnv.png')
