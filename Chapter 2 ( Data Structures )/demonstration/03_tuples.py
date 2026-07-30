"""Chapter 2 - Tuples

This file introduces tuples, which are immutable ordered collections.
"""

print("--- Tuples ---")

point = (3, 5)
print("Point:", point)
print("X coordinate:", point[0])
print("Y coordinate:", point[1])

rgb = (255, 128, 64)
red, green, blue = rgb
print("Red:", red)
print("Green:", green)
print("Blue:", blue)

print("Tuple length:", len(rgb))


a = 10 
b = 20 

a , b = b , a
