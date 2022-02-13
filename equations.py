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

# add # of iterations
def mandelbrot(c):
    for n,z in enumerate(sequence(c)):
        print(f"z({n}) = {z}")
        if n >= 9:
            break
