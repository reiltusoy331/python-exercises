# Write a Python program that calculates the distance between two 3D points.
# The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate.
# The third element is the z-coordinate.

point_A = [3, 4, 5]
point_B = [1, 3, 5]

distance = ((point_A[0]-point_B[0]) ** 2
            + (point_A[1]-point_B[1]) ** 2
            + (point_A[2]-point_B[2]) ** 2) ** (1/2)

print(distance)
