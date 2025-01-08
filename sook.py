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

kysimus= str(input("Mis kell on? "))

x = kysimus.split(":")
kell = int(x[0]) + float(x[1])/60
if  kell >= 7 and kell <=8:
    print("Hommikusöök")
elif kell >= 18 and kell <= 19:
    print("Õhtusöök")
else:
    kell >= 12 and kell <=13
    print("Lõunasöök")

# else:
#     kell >= 12 and kell <=13
#     print("Lõunasöök")
    
#     elif kell >= 18 and kell <= 19




