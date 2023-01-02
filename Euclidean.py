import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
d = math.sqrt((x1-y1) * (x1-y1) + (x2-y2) * (x2-y2) + (x3-y3) * (x3-y3))
print("Distance is: ",d)