#Marii 19.11.2024
#Ülesanne 14

import turtle
ekraan = turtle.Screen()
turtle.speed(0)

def turtle_peale_klikkimine(x, y):
   turtle.penup()
   turtle.goto(x,y)
   turtle.pendown()
   
   for i in range(4):
      turtle.fd(50)
      turtle.lt(90)

def varv_red():
   turtle.color("red")
def varv_green():
   turtle.color("green")
def varv_blue():
    turtle.color("blue")


ekraan.onclick(turtle_peale_klikkimine)
ekraan.onkey(varv_red, "r")
ekraan.onkey(varv_green, "g")
ekraan.onkey(varv_blue, "b")

ekraan.listen()
turtle.mainloop()

