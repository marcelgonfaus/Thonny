#P005_RO025_repte.py
#resultat dels reptes assolits d'una matèria

nexamen= int(input("Nota examen sobre 100 punts: "))
nt1= int(input("Nota tasca1 sobre 10: "))
nt2= int(input("Nota tasca2 sobre 10: "))
nt3= int(input("Nota tasca3 sobre 10: "))
nlliço= int(input("lliçons sobre 10: "))

nlliço= nlliço *2
nexamen= nexamen * 0.7
ntasques= (nt1 + nt2 + nt3)/3

nt= nexamen + nlliço + ntasques

print("nota total= ",nt)