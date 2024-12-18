# 5 
# Shopping List
# Create a program that will keep track of items for a shopping list.
# The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.
# ostukorv = ["õunad", "banaanid", "sai", "keefir", "juust"]
# int(input("Sisestage oma tooted"))
# list = []
# vajalikud_tooted = True

# while True:
#     soovitud_tooted = input("Millist toodet sooviksid lisada? ")
#     list.append(soovitud_tooted)
#     print("Sinu ostukorvis on järgnevad asjad: ")

#     for toode in soovitud_tooted:
#         print("- " + toode)

#         vastus = input("Soovite veel asju ostukorvi lisada? (j/e) ")
#         if vastus == "n":
#             vajalikud_tooted = False

# print("Sinu ostukorvi lõpptulemus on: ")
# for toode in vajalikud_tooted:
#     print("- " + toode)
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




# 3
# Positiivsed ja negatiivsed
# tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
# kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
# nulli lisamisel ei tehta midagi 1p
# väljasta mõlemad loendit 1p


# 6 
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p



# 9
# Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: 'Tere enimi, sinu email on server serveris ja domeeniks on sul com' - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p



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


