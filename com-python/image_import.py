from skimage import io, filters
import os

import numpy as np
import matplotlib.pyplot as plt

from skimage.color import rgb2gray

from mpl_toolkits import mplot3d


image = io.imread('../images/plastic_dark_background.jpg')
image = io.imread('../images/sp5.png')

grayscale = rgb2gray(image)

print(image.shape)
print(dir(image))

edges = filters.sobel(grayscale)
io.imshow(edges)
io.show()

io.imshow(image)
io.show()

print(edges)

fig = plt.figure();
ax = plt.axes(projection='3d')
ax.plot_surface(range(image.shape[0]), range(image.shape[1]), image[1])
plt.show()


