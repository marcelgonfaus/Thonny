#P016_RO041_pi.py

n = int(input("número de termes = "))

k = 1
pi_4 = 0


for i in range(1,n+1):
    terme_n = i
    if terme_n % 2 != 0:
        pi_4 = pi_4 + (1/k)
    if terme_n % 2 == 0:
        pi_4 = pi_4 + (1/k) * (-1)
    k = k + 2
    print("pi_4 = ", pi_4)
    
pi = 4 * pi_4
print("pi = ", pi)