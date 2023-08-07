# Fractal Generators

This project contains Python implementations of algorithms to generate two popular fractals - the Mandelbrot set and the Julia set. Fractals are beautiful and intricate patterns that arise from simple mathematical equations and iterations. These fractals can be visualized and explored using the provided code.

## Prerequisites

Make sure you have the following software installed:

- Python 3.x
- NumPy
- Matplotlib

You can install NumPy and Matplotlib using pip:

```
pip install numpy matplotlib
```

## Mandelbrot Set Generator

The Mandelbrot set is a set of complex numbers generated by iterating a simple mathematical equation. Points in the complex plane are tested to see if the corresponding sequence of values remains bounded or diverges to infinity. Points that remain bounded are considered part of the Mandelbrot set and are colored accordingly.

### Usage

To generate and visualize the Mandelbrot set, run the following command:

```
python mandelbrot_set.py
```

This will produce a plot displaying the Mandelbrot set.

You can adjust the following parameters in the `mandelbrot_set.py` file:

- `width`: Width of the plot in pixels.
- `height`: Height of the plot in pixels.
- `xmin`, `xmax`, `ymin`, `ymax`: Define the rectangular region in the complex plane to visualize.
- `max_iter`: Maximum number of iterations for the Mandelbrot set computation.

## Julia Set Generator

The Julia set is another popular fractal, generated in a similar manner as the Mandelbrot set. However, for the Julia set, the constant 'c' is fixed, and the starting value of 'z' varies across the complex plane. Points in the complex plane are tested to see if their corresponding sequence remains bounded or diverges.

### Usage

To generate and visualize the Julia set, run the following command:

```
python julia_set.py
```

This will produce a plot displaying the Julia set.

You can adjust the following parameters in the `julia_set.py` file:

- `width`: Width of the plot in pixels.
- `height`: Height of the plot in pixels.
- `xmin`, `xmax`, `ymin`, `ymax`: Define the rectangular region in the complex plane to visualize.
- `c`: The constant 'c' for the Julia set computation.
- `max_iter`: Maximum number of iterations for the Julia set computation.

## Additional Notes

- The color maps and visualization parameters can be adjusted in each script to create different visual representations of the fractals.
- Feel free to explore different regions of the complex plane and experiment with various values of 'c' and iteration counts to observe the stunning patterns and details in these fractals.

Enjoy exploring the fascinating world of fractals with this project!
