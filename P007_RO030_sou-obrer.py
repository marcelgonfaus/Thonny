#P007_RO030_sou-obrer.py

h = float(input("Hores = "))
preu_hora = float(input("Preu per cada hora = "))
red = float(input("Reduccions = "))

if h <= 40:
    sou_set = (preu_hora * h) - red
else:
    sou_set = (preu_hora * 40) - red + (1.5 * preu_hora * (h - 40))

print("sou setmanal net = ",sou_set)



