#P010_RO032_conversio-temp.py

t = float(input("temperatura = "))
print(" conversió a ºC = 1")
print(" conversió a ºF = 2")
conversio = int(input("prem 1 ó 2 segons la conversió que vols "))

if conversio == 1:
    tc = (5/9) * (t-32)
    print(t, " ºF són ", tc, " ºC")
elif conversio == 2:
    tf = 32 + (9/5) * t
    print(t, " ºC són ", tf, " ºF")