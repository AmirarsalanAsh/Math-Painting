import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        # Change the values to set the color of the canvas
        self.data[:] = color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
