# ÜLESANNE 4 - Jootraha kalkulaator

# Restoranis on tavaks jätta teenindajale jootraha, mis moodustab tavaliselt vähemalt 15% arve summast.

# Programm küsib kasutajalt summa sõnena formaadis ##.##€ (kus iga # tähistab numbrit), eemaldab euro märgi (€) ja teisendab summa ujukomaarvuks (float).
#  Näiteks, kui kasutaja sisestab 50.00€, tagastab programm 50.0.

# Eeldatakse, et kasutaja sisestab väärtused alati nõutud formaadis.
def teisenda_summa():
    summa_str = input("Sisestage summa ##.##€ formaadis: ")

    summa_float = float(summa_str.replace("€", ""))
    print(f"summa: {summa_float}")
teisenda_summa()



# ÜLESANNE 8 - NämNaäm

# Oletame, et tavaks on süüa:
#     Hommikusööki vahemikus 7:00 – 8:00
#     Lõunasööki vahemikus 12:00 – 13:00
#     Õhtusööki vahemikus 18:00 – 19:00

# Oleks ju tore, kui sul oleks programm, mis ütleb sulle, millal on aeg süüa?
# Failis sook.py loo programm, mis küsib kasutajalt aega ja väljastab, kas on aeg hommikusöögiks, lõunasöögiks või õhtusöögiks. Kui pole söögi aeg, ei väljasta programm midagi.

# Eelda, et kasutaja sisestab aja 24-tunnises formaadis:

#     #:## või ##:##
# Ja eelda, et iga söögiaja vahemik on kaasav. Näiteks, kui aeg on 7:00, 7:01, 7:59 või 8:00, on aeg hommikusöögiks.
# Programmi struktuur peaks olema järgmine:
#     teisenda aeg (str) 24-tunnises formaadis vastavaks arvuks (float).
#     Näiteks, kui antakse aeg "7:30", tagastab funktsioon 7.5.
#     programm kontrollib aja alusel, kas on hommiku-, lõuna- või õhtusöögi aeg, ja väljastab vastava teate.






# ÜLESANNE 9 - Coca-Cola automaat

# Oletame, et automaat müüb Coca-Cola pudeleid hinnaga 50 senti ning aktsepteerib ainult järgmisi mündiväärtusi:
#     25 senti
#     10 senti
#     5 senti

# Failis coke.py loo programm, mis:
#     Küsib kasutajalt korduvalt münti, teatades iga kord, kui palju raha on veel puudu.
#     Kui kasutaja on sisestanud vähemalt 50 senti, arvutab programm ja väljastab tagasiantava raha hulga sentides.
#     Eeldatakse, et kasutaja sisestab alati täisarve. Kui sisestatud väärtus ei ole 25, 10 ega 5, ignoreerib programm seda ja küsib uut sisendit.



