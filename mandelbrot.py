import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]
    z = np.zeros_like(c)

    for i in range(max_iter):
        z = z**2 + c

    mandelbrot = np.abs(z) < 2
    return mandelbrot


width, height = 800, 600
xmin, xmax = -2.5, 1.5
ymin, ymax = -2.0, 2.0
max_iter = 100

mandelbrot = mandelbrot_set(width, height, xmin, xmax, ymin, ymax, max_iter)

plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax),
           cmap='hot', interpolation='bilinear')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
