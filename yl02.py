#Marii 07.10
#Harjutus2


import turtle

aken= turtle.Screen()
aken.title("Sinilill - Marii")
aken.setup(width=500, height=500)
turtle.speed(0)
turtle.pensize(10)

turtle.pencolor("green")
turtle.goto(0,-150)
turtle.left(90)
turtle.fd(200)
turtle.left(-90)
turtle.begin_fill()
turtle.color("blue", "lightblue")
turtle.circle(70)
turtle.left(90)
turtle.end_fill()

turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.penup()
turtle.fd(45)
turtle.pendown()
turtle.right(90)
turtle.circle(25)
turtle.end_fill()
#leht
turtle.penup()
turtle.goto(-20,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color("green", "green")
turtle.left(90)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.end_fill()


turtle.done()
