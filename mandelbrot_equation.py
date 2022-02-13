import numpy as np
import matplotlib.pyplot as plot
# Recursive Approach
def z(n,c):
    if n == 0:
        return 0
    return z(n-1,c)**2 + c

# Iterative Approach
def sequence(c, z=0):
    while True:
        yield z
        z = z**2 + c

def mandelbrot(c):
    for n,z in enumerate(sequence(c)):
        print(f"z({n}) = {z}")
        if n >= 9:
            break

# This returns a 2d array of complex numbers bounded by the params
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    # On a complex plane, the x axis represents the real component
    # whereas the y axis represents the imaginary component
    real = np.linspace(xmin, xmax, int((xmax-xmin) * pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax-ymin) * pixel_density))
    return real[np.newaxis, :] + imaginary[:, np.newaxis] * 1j


# Returns true/false if z value exceeeds or stays within threshold of 2 (in or not in Mandelbrot set)
def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

# Run
c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
members = get_members(c, num_iterations=10)
plot.scatter(members.real, members.imag, color="black", marker=",", s=1)
plot.gca().set_aspect("equal")
plot.axis("off")
plot.tight_layout()
plot.show()