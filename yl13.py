#Marii 19.11.2024
#Ülesanne 13

import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
vanus = screen.numinput("Vanuse sisestamine", "Mis on sinu vanus?", default=20, minval=0, maxval=100)
vanus = 8
cm = 10
mm = 5

for i in range(8):
    for j in range(10):
        t.fd(mm)
        t.lt(90)
        t.fd(mm)
        t.lt(180)
        t.fd(mm)
        t.lt(90)
    t.lt(90)
    t.fd(cm)
    t.write(i+1,font=("Arial",8, "normal"))
    t.lt(180)
    t.fd(cm)
    t.lt(90)

turtle.done()