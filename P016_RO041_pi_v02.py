#P016_RO041_pi_v02.py

n = int(input("número de termes = "))

k = 1
pi_4 = 0

i = 1
while i < n+1:
    terme_n = i
    if terme_n % 2 != 0:
        pi_4 = pi_4 + (1/k)
    if terme_n % 2 == 0:
        pi_4 = pi_4 + (1/k) * (-1)
    k = k + 2
    #print("pi_4 = ", pi_4)
    pi = 4 * pi_4
    i = i + 1

print("pi = ", pi) 
  