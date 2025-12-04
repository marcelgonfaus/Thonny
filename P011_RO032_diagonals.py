# P010_RO032_diagonals.py

print("Introdueix mides del bloc rectangular: \n")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d1 = (a*a + b*b)**(1/2)
d2 = (b*b + c*c)**(1/2)
d3 = (a*a + c*c)**(1/2)

if d1 > d2:
    if d1 > d3:
        print("diagonal major d1 = ", d1)
if d2 > d1:
    if d2 > d3:
        print("diagonal major d2 = ", d2)
if d3 > d1:
    if d3 > d2:
        print("diagonal major d3 = ", d3)

if d1 > d2 and d1 > d3:
    print("diagonal major d1 = ", d1)
if d2 > d1 and d2 > d3:
    print("diagonal major d2 = ", d2)
if d3 > d1 and d3 > d2:
    print("diagonal major d3 = ", d3)