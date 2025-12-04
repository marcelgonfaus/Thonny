#P014_RO041_votacions.py

print("vots a favor: 1")
print("vots en contra: 0")
print("qualsevol altra opció és nula")

n = int(input("número de votacions: "))
vots_si = 0
vots_no = 0
vots_nuls = 0

print("Resolució amb for ")

for i in range(1,n+1):
    print("vot",i," =", end = " ")
    vot = int(input())
    if vot == 1:
        vots_si = vots_si + 1
    elif vot == 0:
        vots_no = vots_no + 1
    else:
        print("opció errònia, vot nul")
        vots_nuls = vots_nuls + 1
print("total de vots: ",n)
print("vots afirmatius: ",vots_si)
print("vots negatius: ", vots_no)
print("vots nuls: ", vots_nuls)

