##tervitus
# print("Tere, maailm!")

# #aasta liblikas
# aasta = 2020
# liblikas = " teelehe-mosaiikliblikas "
# lause_keskosa = "aasta liblikas on"
# lause = str(aasta) + liblikas + lause_keskosa
# print(lause)


# #pilved
# pilevede_korgus = float(input("Kõrgus km: "))
# if pilevede_korgus > 6.0:
#     print("Need on ülemised pilved")

# else:
#     pilevede_korgus < 6.0
#     print("Need ei ole ülemised pilved")


# #bussid
# inimesed = 60
# istekohad= 40

# bussid = inimesed//istekohad
# viimases_bussis = inimesed%istekohad
# if viimases_bussis==0:

# #äratus
# aratus = int(input("Mitu korda äratuskell heliseb: "))

# for i in range(aratus):
#     print("tõuse ja sära!")


# # murelikud lapsevanemad
# ringid = int(input("Sisesta ringide arv: "))
# ringide_arv= 5
# i = 1
# porgandite_arv=0
# while i <= ringid:
#   if i%2==0:
#     print(i)
#   i += 1
# print(f"porgandite koguarv on: {porgandite_arv}")

# #taringud
# import random
# taring= 5
# for i in range(taring):
#     print(random.randint(1,6))

# #male
# taisarv = 10
# nisutera = 0
# korda = taisarv 

# if taisarv > 64:
#     print("Nii palju ruute ei ole")

# if taisarv >= 1:
#     nisutera+=1
#     taisarv-=1

# while korda >= 1:
#     nisutera *=2
#     korda-=1


# #õunad
# import random
# ounad = 14
# poisid = 3
# for i in range(poisid):
#     ounad


#ülikooli vastuvõtud
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
print(vastuvõetud)
fail.close()

a = int(input("Palun sisestage, millise aasta andmeid vajate: "))

print(vastuvõetud(int(a[3])-1))


