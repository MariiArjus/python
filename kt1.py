# 5 
# Shopping List
# Create a program that will keep track of items for a shopping list.
# The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.
"""
poe_list = []
soovitud_tooted = True
while soovitud_tooted == True:
    
    lisatud_tooted = input("Milliseid tooteid soovite lisada?  ")
    poe_list.append(lisatud_tooted)
    print("Teie ostukorvis on järgnevad tooted:  ")
    for toode in poe_list:
        print("-  " + toode)
    
    vastus = input("Soovite veel tooteid lisada? (ja/ei)  ")
    if vastus == "ei":
        soovitud_tooted = False
print("Teie ostukorvi lõpptulemus on:  ")
for item in poe_list:
    print("-  " + toode)
"""

# 3
# Positiivsed ja negatiivsed
# tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
# kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
# nulli lisamisel ei tehta midagi 1p
# väljasta mõlemad loendit 1p
"""
pos = []
neg = []
num = int(input("Sisestage arv: "))
if num > 0:
    pos.append(num)
    print(pos, "see on positiivne arv")
elif num < 0:
    neg.append(num)
    print(neg, "see on negatiivne arv")
"""

# 6 
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p
"""
kysimus = int(input("Palun sisestage arv: "))

if kysimus % 2 == 0:
    print(f"Number {kysimus} on paaris arv")
else:
    print(f"Number {kysimus} on paaritu arv")
"""

# 9
# Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: 'Tere enimi, sinu email on server serveris ja domeeniks on sul com' - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p
def main():
    email = input("Sisestage oma email")

if "@" in email and "." in email.split("@")[-1]:
    print("Sisestatud email on õige")
else: 
    print("Sisestatud email on vale")





# 14. Palkade võrdlus - Loo palk.txt fail töötajate nime, soo ja palganumbriga (10 töötajat).
# 	Koosta programm, mis analüüsib kas firmas toimub diskrimineerimist soo järgi. Selleks võrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kõige kõrgemat palka. Programm peab tegema otsuse.

# 	Hubert Hunt m 2340
# 	Siim Siil m 2570
# 	Märt Mäger m 1960
# 	Vilma Vihmauss n 2060
# 	Merike Metskits n 2250
# 	Kati Karu n 2370
# 	Elmar Elevant m 2900
# 	Timoteus Tigu m 2850
# 	Reet Rebane n 2340
# 	Kalev Kaamel m 2570
# 	Karmen Kass n 2120
# 	Kornelius Koer m 2250




