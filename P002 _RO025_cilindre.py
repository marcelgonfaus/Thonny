#P002 _RO025_cilindre.py

pi = 3.1416

radi = int(input("radi = "))
altura = int(input("altura= "))

print("Àrea i volum d'un cilindre, Dades en cm")
#volum = pi * radi * radi * altura -- #diferents formes de escriure-ho
#volum = pi * radi**2 * altura
volum = round(pi * pow(radi,2) * altura, 3)

print("Volum = ",volum,"cm3")