#P008_RO038_for_n imparells.py

from math import *
n= int(input("numero d'imparells: "))
suma= 0

for i in range(1, n+1):
    k= (2 * i) - 1
    suma = suma + k
print("suma = ",suma)
if suma == pow(n,2):
    print ("verdader")
else:
    print("fals")
