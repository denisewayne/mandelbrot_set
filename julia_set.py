import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

# This returns a 2d array of complex numbers
# Pixel Density = # pixels per unit
def z(xmin, xmax, ymin, ymax, pixel_density):
    real = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j


def iterate(z, c, num_iterations):
    for _ in range(num_iterations):
        z = z**2 + c
    return z


# Returns the complex_matrix as true/false values if z is in the Mandelbrot set (threshold less than 2)
def is_stable(z, c, num_iterations):
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(iterate(z, c, num_iterations)) <= 2


# Filter out numbers in matrix that are True
def get_members(z, c, num_iterations):
    mask = is_stable(z, c, num_iterations)
    return z[mask]


def get_z(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return z


# Create Visual scatterplot of equation
def julia_scatterplot(z, c, num_iterations):
    members = get_members(z, c, num_iterations)
    plot.imshow(is_stable(z, c, num_iterations), interpolation="bicubic", cmap="magma")
    plot.gca().set_aspect("equal")
    plot.axis("on")
    plot.tight_layout()
    plot.show()


# Run
np.warnings.filterwarnings("ignore")
matrix = z(-1, 0.25, -0.75, 0.75, pixel_density=512)
julia_scatterplot(matrix, -0.744 + 0.148j, 20)
