#18.10 Marii
#Ülesanded 5

import random
import turtle
#4. Mündiviskamise äraarvamine koos juhuslikkusega
mynt = random.randint(0,1)
arva = input("Vali kull või kiri: ")
if (mynt == 0 and arva == "kiri") or (mynt == 1 and arva == "kull"):
    vastus ="green"
else:
    vastus= "red"
print(mynt)
turtle.color(vastus)
turtle.circle(100)
turtle.done()




"""
#3. Vanusepiiranguga üritus

vanus = int(input("Lisa vanus: "))
if vanus >= 18:
    print("Saab sisse!")
else:
    print("Liiga noor!")
"""

"""
import random
#2. Matemaatika test
a = random.randint(1,10)
b = random.randint(1,10)
vastus = int(input(str(a)+"*"+str(b)+"="))
if a*b== vastus:
    print("Tubli!")
else:
    print("Vale!")
"""

"""
#1. Ilmaennustuse rakendus

try:
c = int(intput("Lisa kraadid: "))
if c < 0:
    print("Kanna tarveriideid")
elif c>=0 and c<=15:
    print("Kanna kevad-sügis rõivaid")
else:
    print("Kanna suveriideid")
except:
    print("Pane täisarv")
"""