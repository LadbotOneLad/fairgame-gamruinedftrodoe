import numpy as np

# Define resolution and complex constant c for the Julia set
width, height = 80, 40
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.0, 1.0
c = complex(-0.7, 0.27015)
max_iter = 255

# Generate complex matrix coordinate plane
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Matrix iteration loop
img = np.zeros(Z.shape, dtype=int)
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + c
    img[mask] += 1

# Render mathematical fractal directly to terminal characters
chars = " .:-=+*#%@"
for row in img:
    print("".join(chars[val % len(chars)] for val in row))
