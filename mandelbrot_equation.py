import numpy as np
import matplotlib.pyplot as plot
from PIL import Image

# This returns a 2d array of complex numbers
# Pixel Density = # pixels per unit
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    real = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j


# Returns the complex_matrix as true/false values if z is in the Mandelbrot set (threshold less than 2)
def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2


# Filter out numbers in matrix that are True
def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


# Create Visual scatterplot of equation
def mandelbrot_scatterplot(c, num_iterations):
    members = get_members(c, num_iterations)
    # plot.scatter(members.real, members.imag, color="black", marker="1", s=1)
    plot.imshow(is_stable(c, num_iterations), cmap="binary")
    plot.gca().set_aspect("equal")
    plot.axis("on")
    plot.tight_layout()
    plot.show()


# Run
np.warnings.filterwarnings("ignore")
matrix = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=612)
image = Image.fromarray(~is_stable(matrix, 20))
# image.show()
Image.effect_mandelbrot((512, 512), (-3, -2.5, 2, 2.5), 100).show()
# mandelbrot_scatterplot(matrix, 20)
