#Marii 28.11.2024 ül17

# #Pangatehing
# # kogu tehingute arvu
# # positiivsete tehingute arvu
# # positiivsete tehingute kogusumma

# fail=open("pangakonto.txt")
# tekstiread = fail.readlines()
# tehingute_arv = len(tekstiread)
# pos_tehingud = 0
# pos_tehingute_summa = 0

# for i in tekstiread:
#     if float(i) > 0:
#         pos_tehingud+=1
#         pos_tehingute_summa+=i

# print(f"Tehinguid kokku: {tehingute_arv}")
# print(f"Pos tehinguid kokku: {pos_tehingud}")
# print(f"Tehingute summa: {pos_tehingute_summa}")


#Palgastatistika
# meeste keskmised töötunnid, töötasu ning palk
# naiste keskmised töötunnid, töötasu ning palk

fail = open("palgad.txt")
tekstiread = fail.readlines()
mpalgad = []
npalgad = []



for i in tekstiread:
    sugu = i.split(",")[3]
    palk = i.split(",")[6]
    if sugu== "Mees":
        mpalgad.append(float(palk))
    else: 
        npalgad.append(float(palk))

mkeskmine = sum(mpalgad)/len(mpalgad)
print(f"Meeste keskmine palk on {mkeskmine}")

nkeskmine = sum(npalgad)/len(npalgad)
print(f"Naiste keskmine palk on {nkeskmine}")





