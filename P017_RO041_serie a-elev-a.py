#P017_RO041_serie a-elev-a.py

suma = 0
x = int(input("x = "))
a = 1
while suma < x:
    suma = suma + a**a
    print(suma)
    a = a + 1
print("numero de termes = ",a)
    
    
