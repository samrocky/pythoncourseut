r = float(input())
h = float(input())
pi = 3.14
area = (pi*r**2)+(pi*r)*((r**2+h**2)**0.5)
surface = (2*pi*r)+(pi*r)*((r**2+h**2)**0.5)

print(area)
print(surface)
