#Marii 8.11.2024
#Harjutus 10
import random
#Arvude keskmine
# arvud= []
# loop = 1

# while loop==1:
#     arv= input("Sisesta arv: ")
#     if arv == "":
#         loop = 0
#         break
#     arvud.append(int(arv))



# print(sum(arvud)/len(arvud))

#Arvu äraarvamise mäng
#2

katsed=0
loop = 1
arv = random.randint(1,10)
print(arv)
while loop==1:
    katsed+=1
    vastus= int(input("Arva ära arv 1-10: "))
    if vastus ==arv:
        print("Õige!")
        uuesti = input("Kas soovid veel (j/e): ")
        if uuesti== "j":
            katsed: 0
        else:
            break
    else:
        print("Proovi uuesti")

print(f"Arvasid {katsed} ära")

