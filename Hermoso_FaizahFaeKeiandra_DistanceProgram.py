import math

# Ask the user their input for their two points.
point_x1 = float(input("Enter the x1:  "))
point_x2 = float(input("Enter the x2:  "))
point_y1 = float(input("Enter the y1:  "))
point_y2 = float(input("Enter the y2:  "))

# Ask the user to put the formula for the distance.
point_a = pow(point_x2-point_x1, 2)
point_b = pow(point_y2-point_y1, 2)
result = point_a + point_b
distance = math.sqrt(result)

# Ask the user to print the final distance.
print("\nThe distance is", distance)
