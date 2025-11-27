#P006_RO035_if.py

n = int(input("quantitat de pneumàtics: "))
p = int(input("preu inicial de cada pneumàtic (€): "))

if n > 4:
    p = 0.9 * p
    print("cost total= ",n * p)