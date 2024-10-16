# 16.10.2024
# Ülesanded 4
import turtle
#Ringi pindala ja Turtle
r = 10
s = 3.14*r**2
p = 2 * 3.14 * r
print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
turtle.circle(r*10, 360)
turtle.done()
#Kingituste pakkimine
try:
    kast = 5
    KingitusteArv = int(input("Lisa kingituste arv : "))
    komplektid = KingitusteArv// kast #täisarvu saamine
    yle = KingitusteArv%kast #jäägi saamie
    print(f"Saad teha {komplektid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print("Lisasid koguse valesti")

#Faili allalaadimine
try:
    failiSuurus=int(input("Sisesta faili suurus : "))
    downlKiirus= int(input("Sisesta allalaadimise kiirus  : "))
    aeg= failiSuurus/downlKiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except: 
    print("Palun sisestage täisarvud!")

#Raamatute allahindlus
ale = 0.3
hind= 12.3
kogus= int(input("Lisa raamatute kogus : "))
summa = (hind- (hind*ale)) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.")

#Aia pikkus
a = int(input("lisa 1 külg: "))
b = int(input("lisa 2 külg: "))
p = 2 * (a + b)
print(f"aia kogupikkus on {p} meetrit")
