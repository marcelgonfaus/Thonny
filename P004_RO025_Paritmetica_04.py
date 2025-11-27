#PO04_RO025_Paritmetica_04.py
n = 0
print("Menú Progressio Aritmètica")
print("===============================  ")
print("Prem l'opció de càlcul:")
print("Opció 1: darrer terme an")
print("Opció 2: darrer terme an")
print("Opció 3: numero de termes an")
print("Opció 4: diferencia o raó d")
opcio = int(input("Prem l'opció entre 1 i 4: "))
#--------------------------------------------------------
if opcio == 1:
    a1 = eval(input("a1 = "))
    n = int(input("n = "))
    d = eval(input("d = "))
    
    iteracions = n
    n = 1
    while n <= iteracions:
        an = a1 + (n-1) * d
        print(round(an,2),end = " ")
        n = n + 1
    
if opcio == 2:
    an = eval(input("a1 = "))
    n = int(input("n = "))
    d = eval(input("d = "))

    iteracions = n
    n = 1
    while n <= iteracions:
        a1 = an - (n-1) * d
        print(round(a1,2),end = "  ")
        n = n + 1
    
if opcio == 3:
    an = eval(input("an = "))
    a1 = eval(input("a1 = "))
    d = eval(input("d = "))
    
    n = ((an-a1)/d) + 1
    
    if n == int(n):
        print("n = ",int(n))
    else:
        print("El número de termes ha de ser un sencer")
    
    
