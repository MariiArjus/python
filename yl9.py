#24.10 Marii
#Ülesanne 9

import random
"""
# Genereeri ja kuva arvud arvud 1-20
for i in range (1,21):
    print(i, end=" ")


# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
for i in range(1,21):
    print(random.randint(1,100), end=" ")
print()

# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
## Leia paaris ja paaritud arvud ning lisa oma loendisse
## Kuva paaris ja paritute arvude summad
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []
for i in loend:
    if i %2==0:
        paaris.append(i)
    else:
        paaritud.append(i)


print(f"Paaris arvuse summa: {sum(paaris)} ")
print(f"Paaritute arvude summa: {sum(paaritud)}")
"""

# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

for i in range (1,43):
    if 1%3==0 and i%5==0:
        print(i,"tiktak", end=" ")
    elif i%3==0:
        print(i,"TIK", end=" ")
    elif i%5==0:
        print(i,"TAK", end=" ")
    else: 
        print(i, end=" ")

print()
# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale. 

for i in range (200,321):
    if i%7==0 and i%5>0:
        print(i, end=" ,")







# random.randint(min, max)

# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
# Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# Näiteks:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Loo programm, mis loob suvalised tehted 1-100 arvudega.
# Kasuta tsükli puhul alakriipsu
# kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
# Näiteks:
# 7 – 2=
# 45 * 69=
# 71 – 45=
# 84 / 57=
# 59 * 87=
# 84 – 71=
# 65 * 32=
# 63 – 11=
# 72 – 90=
# 29 / 93=
# Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
# Õiged vastused loetakse kokku
# # Kui saab vähemalt poole punktid, siis saab A, muul juhul MA
