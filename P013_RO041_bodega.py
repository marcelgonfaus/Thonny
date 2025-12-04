#P013_RO041_bodega.py

n = int(input("número de paquets: "))
pes_maxim = 0
i = 1
while i <= n:
    print("pes del paquet ",i, " en kg:", end = " ")
    pes = int(input())
    if pes > pes_maxim:
        pes_maxim = pes
    i = i + 1
print("Pes màxim : ", pes_maxim, " kg")
    