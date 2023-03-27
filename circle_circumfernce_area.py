# Calculator to calculate area / circumference
# Read radius as input from the user

import math

# Circumference: 2 * pi * R
# Area: pi * R * R

radius = int(input("Please enter radius: \n"))

circumference = 2 * math.pi * radius
area = math.pi * radius * radius
print(f"circumference of the circle is: {circumference}")
print(f"area of the circle is: {area}")