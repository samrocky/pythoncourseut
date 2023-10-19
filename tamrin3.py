a = 5.5
t = 5
v0 = 5.25
x0 = float(input())
x1 = ((1/2)*(a*(t**2)))+(v0*t)+x0
#-----------------------------
a = 5.25
t = 5.5
v0 = float(input())
v1 = (a*t)+v0
#-----------------------------
v2 = 10
v0 = 5
deltax = float(input())
a1 = ((v2**2)-(v0**2))/(2*deltax)
#-----------------------------
v0 = 5.25
v2 = float(input())
vavg1 = (v2 + v0)/2
#-----------------------------
v0 = 5.5
t0 = 5
v2 = 55
t2 = float(input())
deltax1 = ((v2+v0)/2)*(t2-t0)
#-----------------------------
print(x1)
print(v1)
print(a1)
print(vavg1)
print(deltax1)