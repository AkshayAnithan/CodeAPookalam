from turtle import *
import turtle
turtle.speed(0)
turtle.home()
screen = Screen()
screen.screensize(400,400,"white")

def circ(cl,r): 
    turtle.begin_fill()
    turtle.fillcolor(cl)
    turtle.speed(0)
    turtle.pen(pencolor=cl,pensize="1")
    turtle.pu()
    turtle.rt(90)
    turtle.fd(r)
    turtle.left(90)
    turtle.down()
    turtle.circle(r)
    turtle.end_fill()
    turtle.pu()
    turtle.home()
    turtle.down()

def square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)

def big_flower(shade):
    for i in range(13):
        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.fillcolor(shade)
        turtle.pen(pencolor=shade,pensize="1")
        turtle.begin_fill()
        turtle.circle(305,70)
        turtle.left(110)
        turtle.circle(305,70)
        turtle.end_fill()
        turtle.right(1)

def draw_square(square,lll,cll):
    for i in range(0,2):
        square.begin_fill()
        square.fillcolor(cll)
        square.forward(lll)
        square.right(30)
        square.forward(lll)
        square.right(150)
        square.end_fill()


def draw_flower(coll,sizz):
	window = turtle.Screen()
	window.bgcolor("white")
	hello = turtle.Turtle()
	hello.speed(0)
	hello.shape("triangle")
	hello.color(coll)
	for i in range(0,36):
		draw_square(hello,sizz,coll)
		hello.right(10)

def petal(t, r, angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)

def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

def petal(my_radius,my_petals,c):
    for _ in range(my_petals):
        ak.color(c)
        ak.fillcolor(c)
        ak.begin_fill()
        draw_petal(ak, my_radius)
        ak.left(360 / my_petals)
        ak.end_fill()
        ak.hideturtle()

turtle.pen(pencolor="#770E13",pensize="1")
circ("#770E13",400)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",390)
turtle.pen(pencolor="#ECE19F",pensize="1")
circ("#ECE19F",380)
turtle.begin_fill()
turtle.pen(pencolor="red",pensize="1")
turtle.fillcolor("red")
turtle.speed(0)
turtle.pen(pencolor="red",pensize="1")
for k in range(40):
    square(270)
    turtle.rt(10)
turtle.end_fill()
turtle.pen(pencolor="orange",pensize="1")
circ("orange",350)
turtle.pen(pencolor="#383629",pensize="1")
big_flower("#383629")
turtle.right(60)
turtle.pen(pencolor="#EFE19A",pensize="1")
big_flower("#EFE19A")
turtle.pen(pencolor="#C8520A",pensize="1")
turtle.right(60)
big_flower("#C8520A")
turtle.pen(pencolor="red",pensize="1")
circ("red",280)

t = turtle.Turtle()
t.speed(0)

turtle.begin_fill()
turtle.pen(pencolor="#ECE19F",pensize="1")
turtle.fillcolor("#ECE19F")
turtle.speed(0)
turtle.pen(pencolor="#ECE19F",pensize="1")
turtle.end_fill()

turtle.pen(pencolor="#F4E389",pensize="1")
circ("#F4E389",250)
draw_flower("orange",129)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",220)
turtle.pen(pencolor="#2E7644",pensize="1")
circ("#2E7644",210)

turtle.begin_fill()
turtle.pen(pencolor="orange",pensize="1")
turtle.fillcolor("orange")
#draw_flower()
for k in range(40):
    square(148)
    turtle.rt(10)
turtle.end_fill()
turtle.speed(0)
turtle.pen(pencolor="#F4E389",pensize="1")
circ("#F4E389",160)
turtle.speed(0)
turtle.begin_fill()
turtle.pen(pencolor="red",pensize="1")
turtle.fillcolor("red")

#draw_flower()
for k in range(9):
    for i in range(6):
        turtle.forward(100) 
        turtle.right(60) 
    turtle.rt(40)
turtle.end_fill()
turtle.pen(pencolor="#C8520A",pensize="1")
circ("#C8520A",172)
turtle.pen(pencolor="#770E13",pensize="1")
circ("#770E13",162)
turtle.pen(pencolor="#E67B47",pensize="1")
circ("#E67B47",152)
turtle.pen(pencolor="orange",pensize="1")

size=300

ak = Turtle()
pen = Pen()
ak.speed(1000)
pen.speed(1000)

flag=0

def fillshape(steps,radius,c1,c2):
    if(flag==0):
        c2=c1
    pen.color(c1)
    pen.fillcolor(c2)
    pen.begin_fill()
    pen.down()
    if(steps!=0):
        pen.circle(radius,steps=steps)
    else:
        pen.circle(radius)
    pen.end_fill()
    pen.up()
    pen.hideturtle()

pen.goto(0,-size)
c1="black"
c2="black"

pen.goto(0,0)
x=0
turtle.delay(0)
colormode(255)
no=12
    
x=30
pen.right(15)
pen.pensize(10)

pen.left(15)
pen.width(1)
for i in range(no*3):
        
    if(i<no):
        pen.goto(0,0)
        c1="mediumpurple"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*2):
        pen.goto(0,0)
        c1="darkgreen"
        fillshape(4,90,c1,c2)
        pen.right(30)

    elif(i<no*3):
        pen.goto(0,0)
        c1="mediumslateblue"
        fillshape(4,90,c1,c2)
        pen.right(30)

    if(i%no==11):
        pen.right(12)

size2 = 150
pen.goto(0,-size2)
pen.left(35)

ak.speed(1000)

#headacc
pen.width(4)
pen.down()
pen.goto(54,24)
pen.color('darkslateblue')
pen.fillcolor('darkgreen')
pen.begin_fill()
pen.left(45)
pen.circle(80,270)
pen.up()
pen.end_fill()

p = Turtle()
p.speed(20)
x=18

p.speed(3)
p.color('maroon')

for i in range(12):
    if(i>5):
        x+=7
        y=12-i
    else:
        x+=6
        y=i

    p.up()
    p.goto(1,x)
    p.down()
    p.write("*"*y,align='center',font=("Arial", 50, "normal"))

p.color('teal')
x=18

for i in range(8):
    if(i>5):
        x+=7
        y=12-i
    else:
        x+=6
        y=i

    p.up()
    p.goto(1,x)
    p.down()
    p.write("*"*y,align='center',font=("Arial", 50, "normal"))

petal(150,12,'crimson')
petal(110,12,'black')
petal(70,12,'teal')

p.width(4)
p.speed(2000)

flag=1

#greenstruct
p.up()
p.goto(0,5)
p.down()
p.color('seagreen')
p.fillcolor('seagreen')
p.begin_fill()
p.goto(0,5)
p.goto(-50,5)
p.goto(-70,15)
p.goto(-70,-40)
p.goto(-30,-70)
p.goto(30,-70)
p.goto(70,-40)
p.goto(70,15)
p.goto(50,5)
p.goto(0,5)
p.end_fill()
p.up()

#cheek semicircles
p.color("black")
p.fillcolor('limegreen')
p.goto(-45,-60)
p.down()
p.left(60)
p.begin_fill()
p.circle(30,120)
p.goto(-71,-41)
p.end_fill()
p.up()
p.goto(70,-18)
p.down()
p.begin_fill()
p.circle(30,120)
p.goto(71,-41)
p.end_fill()
p.up()
p.goto(25,-71)
p.down()
p.left(160)
p.begin_fill()
p.circle(25,160)
p.up()
p.goto(0,-71)
p.end_fill()
p.up()

#eyebrows
p.up()
p.goto(-20,30)
p.color("forestgreen")
p.down()
p.goto(-4,18)
p.goto(4,18)
p.goto(20,30)
p.goto(40,30)
p.goto(70,55)
p.color('tomato')
p.goto(35,60)
p.color('forestgreen')
p.goto(0,21)
p.goto(-35,60)
p.color('tomato')
p.goto(-70,55)
p.color('forestgreen')
p.goto(-40,30)
p.goto(-20,30)
p.up()

p.goto(30,60)
p.down()
p.begin_fill()
p.goto(35,42)
p.goto(18,42)
p.end_fill()
p.up()
p.goto(-30,60)
p.down()
p.begin_fill()
p.goto(-35,42)
p.goto(-18,42)
p.end_fill()

p.width(3)
#nose
p.goto(0,18)
p.down()
p.color('black')
p.fillcolor('forestgreen')
p.begin_fill()
p.goto(-15,-5)
p.goto(15,-5)
p.goto(0,18)
p.end_fill()

#mouth
p.up()
p.goto(-15,-25)
p.fillcolor('firebrick')
p.begin_fill()
p.down()
p.goto(18,-25)
p.goto(7.5,-14)
p.goto(0,-25)
p.goto(-7.5,-14)
p.goto(-18,-25)
p.end_fill()
p.fillcolor('crimson')
p.begin_fill()
p.goto(0,-35)
p.goto(18,-25)
p.goto(-18,-25)
p.end_fill()
p.goto(18,-25)
p.left(20)
p.begin_fill()
p.circle(5)
p.end_fill()
p.goto(-18,-25)
p.left(180)
p.begin_fill()
p.circle(5)
p.end_fill()

p.speed(1000)

#eyes
p.up()
p.goto(12,16)
p.color('khaki')
p.fillcolor('khaki')
p.down()
p.begin_fill()
p.goto(22,24)
p.goto(40,24)
p.goto(34,18)
p.goto(12,16)
p.end_fill()
p.up()
p.goto(-12,16)
p.down()
p.begin_fill()
p.goto(-22,24)
p.goto(-40,24)
p.goto(-34,18)
p.goto(-12,16)
p.end_fill()
p.color('black')
p.fillcolor('black')
p.up()
p.goto(-22,24)
p.left(30)
p.down()
p.begin_fill()
p.circle(5)
p.end_fill()
p.up()
p.goto(22,24)
p.left(110)
p.down()
p.begin_fill()
p.circle(5)
p.end_fill()

#forehead
p.up()
p.goto(0,22)
p.color("goldenrod")
p.fillcolor("goldenrod")
p.begin_fill()
p.down()
p.goto(-35,60)
p.color('tomato')
p.goto(35,60)
p.color('goldenrod')
p.goto(0,22)
p.end_fill()

p.width(2)
p.up()
p.fillcolor('crimson')
p.goto(20,60)
p.down()
p.begin_fill()
p.goto(0,60)
p.goto(12,40)
p.end_fill()
p.up()
p.goto(-20,60)
p.down()
p.begin_fill()
p.goto(0,60)
p.goto(-12,40)
p.end_fill()
p.up()
p.fillcolor('maroon')
p.begin_fill()
p.goto(0,57)
p.down()
p.goto(10,43)
p.goto(0,30)
p.goto(-6,40)
p.end_fill()

#circle
p.width(15)
p.color('darkgreen')
p.fillcolor('orange')
p.goto(-60,70)
p.down()
p.begin_fill()
p.left(180)
p.circle(20)
p.end_fill()
p.width(3)
p.color('teal')
p.circle(20)
p.up()
pen.width(2)
for i in range (9):
    pen.goto(-78,80)
    c1="forestgreen"
    fillshape(2,14,c1,c2)
    pen.right(40)
p.up()
p.width(15)
p.color('darkgreen')
p.fillcolor('orange')
p.goto(60,70)
p.down()
p.begin_fill()
p.right(100)
p.circle(20)
p.end_fill()
p.width(3)
p.color('teal')
p.circle(20)
p.up()
pen.width(2)
for i in range (9):
    pen.goto(72,86)
    c1="forestgreen"
    fillshape(2,14,c1,c2)
    pen.right(40)

p.color('black')
p.up()
p.goto(1,40)
p.down()
p.write("*",align='center',font=("Arial", 55, "normal"))

turtle.exitonclick()