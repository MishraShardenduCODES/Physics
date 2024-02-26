from vpython import *

# Create a box
box(length=5, width=4, height=3, color=color.blue)

# Create a sphere
sphere(radius=2, color=color.red, pos=vector(6, 0, 0))

# Create a cylinder
cylinder(radius=1, length=5, color=color.green, pos=vector(-6, 0, 0))

# Create an arrow
arrow(pos=vector(0, 0, 0), axis=vector(0, 5, 0), color=color.yellow)