from math import sqrt
r = float(input())
h = float(input())
pi = 3.14
area = (pi*(r**2))+(pi*r*sqrt((r**2)+(h**2)))
surface = (2*pi*r)+(pi*r*sqrt((r**2)+(h**2)))
print(area)
print(surface)