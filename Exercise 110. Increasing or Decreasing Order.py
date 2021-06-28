# Write a Python program that determines if three numbers (a, b, and c) are in increasing order, decreasing order, or none.
# If a > b > c, print "Decreasing Order".
# If a < b < c, print "Increasing Order".
# Else, print "None".

a = 1
b = 2
c = 3

if (a > b) and (b > c):
    print("Decreasing Order")
elif (a < b) and (b < c):
    print("Increasing Order")
else:
    print("None")
