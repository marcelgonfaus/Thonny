#Cilindre_2

from math import *

print ("Càlcul del dìametre d'un cilindre")

v = float(input("Volum del cilindre en dm3: "))
h = float(input("Alçada del cilindre m: "))
v=v/1000
d = (sqrt(v/(h*pi)))*2

print("Diàmetre = " , d , "m")


