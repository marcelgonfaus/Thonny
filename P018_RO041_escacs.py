#P018_RO041_escacs.py

a = 1
suma = 0
while a <= 64:
    suma = suma + 2**a
    print("terme",a,"  suma = ",suma)
    a = a + 1

m_kg = suma / 20000
print("massa en kg = ",m_kg)
m_t = m_kg / 1000
print("massa en tones = ",m_t)
    