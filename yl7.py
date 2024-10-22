#22.10.24 Marii
#ülesanne 7 Massiivid

#Aastaajad
kuud= [('jaanuar',3,-20,1,6,3,1,-19,4,0,-16,-5,-9,-3,-19,-16,-2,-5,-3,-12,-13,3,-15,-18,-11,8,-16,5,9,-5,-8,-11),
('veebruar',-15,-12,10,-12,-11,-16,4,-19,-6,-11,-7,-5,-19,-15,-1,-3,8,8,5,1,-7,8,-1,-13,-16,7,-17,-17),
('märts',7,-17,-20,-9,-4,-6,-5,-2,-20,3,-7,3,-13,-15,-7,-14,-5,-10,-10,10,-5,-15,-8,-9,-19,-2,-16,-15,-3,-8,5),
('aprill',-2,-9,5,-19,-19,3,-11,5,-6,3,-14,3,-19,5,0,6,7,-19,6,-17,10,-11,-1,-19,-17,0,7,-12,-20,-13),
('mai',-7,-19,-13,-9,-11,7,0,3,4,-6,4,-17,-11,-7,-9,-19,-5,2,-17,-6,-7,5,-10,-4,2,-17,0,-9,6,3,0),
('juuni',-16,-4,-19,-1,8,-6,-16,4,-5,-18,-15,-19,2,10,-13,-8,2,-11,2,-15,8,-12,-6,-4,-11,-19,-6,3,-12,5),
('juuli',-15,-9,-11,-8,2,6,-7,-1,0,-17,-14,3,-6,-9,-2,0,-12,-2,-3,9,-8,-16,6,4,5,0,-12,3,-14,-10,1),
('august',-4,-17,8,-15,9,3,-11,2,-7,-4,-2,7,4,7,-11,-5,-9,4,4,-19,-1,-6,9,3,7,-5,-20,-14,-20,-20,-1),
('september',9,-9,1,-1,-6,2,-8,-5,3,-19,-17,5,-10,3,-11,7,-19,-19,7,-9,-2,-19,-13,-8,-12,-12,9,-3,-14,-89),
('oktoober',-19,-5,-6,10,0,2,-20,-16,-16,-10,9,10,1,2,1,-3,0,5,-2,9,5,-9,5,-5,-3,-17,-9,-3,3,7,-12),
('november',-2,-3,-5,-19,9,-10,-17,-14,-1,-9,0,1,-4,-7,7,4,-11,10,-19,-19,4,-3,-5,2,-1,4,-18,-5,-6,9),
('detsember',-14,9,-6,-15,-12,-13,5,2,-9,8,-7,-9,-15,3,-12,-15,-7,-13,-15,-2,-11,-18,3,-4,-4,-3,-3,3,0,-16,-2)]

print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(f"Viimane mõõtmine: {kuud[9][len(kuud[9])-1]} ")
print("Selle kuu temp:")
ajutine = []
for i in range(kuus_kokku):
    ajutine.append(kuud[9][i+1])
    print(kuud[9][i+1], end=", ")
print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")

print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(f"-20 esineb {ajutine.count(-20)} korda: ")

ajutine.pop(5-1)

ajutine.insert(5-1,43)
ajutine.sort()
print(ajutine)




"""
#Muusikapalad
laulud = ['ALIKA –"Bridges"','Anett x Fredi –"Read Between The Lines"','villemdrillem –"leekiv armastus"','Clicherik & Mäx –"PAKSUD"','nublu –"ära ärata"','NOËP –"Move Your Feet"','Trad.Attack! –"Bring It On"','Bedwetters –"It Is What It Is"','Reket –"Panama paberid"','Grete Paia –"Võluväel"']


for i in range(10):
    print(str(i+1)+". "+laulud[i])

try:
    valik = int(input("Vali lugu 1-10: ")-)
    print(f"Mängin: {laulud[valik-1]}")
except:
    print("Tegid vale otsuse:( ")
"""