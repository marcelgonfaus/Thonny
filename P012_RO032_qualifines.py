#P011_RO032_qualifines.py

q1 = float(input("quali 1 = "))
q2 = float(input("quali 2 = "))
q3 = float(input("quali 3 = "))

if q1 > q2 and q2 > q3:
    print("major qualificació = ",q1)
if q2 > q3 and q2 > q1:
    print("major qualificació = ",q2)
if q3 > q1 and q3 > q2:
    print("major qualificació = ",q3)