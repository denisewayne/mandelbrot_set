import numpy as np
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

# Run
mandelbrot(1)

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    # On a complex plane, the x axis represents the real part of the equation
    # whereas the y axis represents the imaginary parts
    real = np.linspace(xmin, xmax, int((xmax-xmin) * pixel_density))
    imaginary = np.linspace(ymin, ymax, int((ymax-ymin) * pixel_density))