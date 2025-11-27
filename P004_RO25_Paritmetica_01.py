#P004_RO25_Paritmetica_01.py
#EXERCICI 15 LLIBRE MATES

a1=-203
an=902.5 #terme enéssim
d=16.5

n=((an-a1)/d)+1
print("n= ",n)
print()

k=n

n=1
s=0
print("n			a			s			\n")

while n < k+1:
    a=a1+(n-1)*d
    s=a+s
    print(n,"               ",a,"         ",        s)
    #printt(S, end = " ")
    n=n+1