import numpy as np
import matplotlib.pyplot as plt


def julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    z = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    for i in range(max_iter):
        z = z**2 + c

    julia = np.abs(z) < 2
    return julia


width, height = 800, 600
xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
c = complex(-0.8, 0.156)
max_iter = 100

julia = julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)

plt.imshow(julia, extent=(xmin, xmax, ymin, ymax),
           cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.title("Julia Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
