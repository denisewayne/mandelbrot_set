import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# JULIA SET fixes value for c and sets a different Initial Condition than Mandelbrot
x_start, y_start = -2, -2  # an interesting region starts here
width, height = 4, 4  # for 4 units up and right
density_per_unit = 200  # how many pixles per unit

# real and imaginary axis
re = np.linspace(x_start, x_start + width, width * density_per_unit)
im = np.linspace(y_start, y_start + height, height * density_per_unit)


threshold = 40  # max allowed iterations
frames = 100  # number of frames in the animation

# we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
r = -1
a = np.linspace(0, 2 * np.pi, frames)

fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw for the photo size
ax = plt.axes()  # create an axes object


def julia_quadratic(zx, zy, cx, cy, threshold):
    """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y
    belongs to the Julia set. In order to belong, the sequence
    z[i + 1] = z[i]**2 + c, must not diverge after 'threshold' number of steps.
    The sequence diverges if the absolute value of z[i+1] is greater than 4.

    :param float zx: the x component of z[0]
    :param float zy: the y component of z[0]
    :param float cx: the x component of the constant c
    :param float cy: the y component of the constant c
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)

    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.0:
            return i

    return threshold - 1  # it didn't diverge


def animate(i):
    ax.clear()  # clear axes object
    # ax.set_xticks([], [])  # clear x-axis ticks
    # ax.set_yticks([], [])  # clear y-axis ticks

    # Julia set does not move when c is constant because the equation is not affected by iteration
    X = np.empty((len(re), len(im)))  # the initial array-like image

    # the i is references to the index between frame # over [0,2pi]
    # ( what value of c to show as it revolves around a circle)
    cx, cy = r * np.cos(a[i]), r * np.sin(a[i])  # the initial c number
    # cx, cy = 0.3 + 0.6 * i, 0

    # graph this specific index of c in a circle iterated over a fixed time
    # iterations for the given threshold
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = julia_quadratic(
                re[i], im[j], cx, cy, threshold
            )  # shows the transformed graph per iteration

    img = ax.imshow(X.T, interpolation="gaussian", cmap="BuGn")
    return [img]


anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
anim.save("julia_set.gif", writer="pillow")
