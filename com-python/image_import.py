from skimage import io, filters
import os

import numpy as np
import matplotlib.pyplot as plt

from skimage.color import rgb2gray

image = io.imread('../images/plastic_dark_background.jpg')
grayscale = rgb2gray(image)

print(image.shape)
print(dir(image))

edges = filters.sobel(grayscale)
io.imshow(edges)
io.show()

io.imshow(image)
io.show()


