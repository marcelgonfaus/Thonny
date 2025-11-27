#P008_RO035_bacteris.py

nbacteris = int(input( "nº de bacteris = "))
maxbacteris = int(input("numero maxim de bacteris = "))
dia = 0 #condicions inicials

while nbacteris <= maxbacteris:
    print("dia", dia, "nbacteris = ", nbacteris)
    nbacteris= nbacteris*2
    dia= dia + 1
print("dia", dia, "nbacteris = ",nbacteris)
