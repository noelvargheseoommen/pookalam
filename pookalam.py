import  turtle

s=turtle.Turtle()
s.speed(100)


s.forward(200)
s.left(90)
s.color('spring green','spring green')
s.begin_fill()
s.circle(200)
s.end_fill()

s.left(90)
s.forward(18)
s.right(90)
s.color('black','black')
s.begin_fill()
s.circle(180)
s.end_fill()

s.left(90)
s.forward(10)
s.right(90)
s.color('white','white')
s.begin_fill()
s.circle(170)
s.end_fill()

s.left(90)
s.forward(170)
s.color('gold','gold')


s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
    s.forward(120)
    s.left(90)
s.end_fill()

s.left(30)
s.color('orange','orange')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
    s.forward(110)
    s.left(90)
s.end_fill()


s.left(30)
s.color('dark red','dark red')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
    s.forward(100)
    s.left(90)
s.end_fill()

s.left(30)
s.color('lime green','lime green')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
    s.forward(90)
    s.left(90)
s.end_fill()

s.left(30)
s.color('khaki','khaki')

s.begin_fill()
for i in range(30):
    s.left(12)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
    s.forward(85)
    s.left(90)
s.end_fill()


for i in range(4):
    for colours in{"gold","orange"}:
       s.speed(100)
       s.color(colours)
       s.begin_fill()
       s.circle(50)
       s.left(50)
       s.end_fill()

for i in range(8):
       
       s.begin_fill()
       s.color("dark red","dark red")
       s.circle(40)
       s.left(50)
       s.end_fill()


s.left(90)
s.penup()
s.backward(30)
s.pendown()
s.right(90)
s.color('black','black')
s.begin_fill()
s.circle(30)
s.end_fill()


s.left(90)
s.forward(8)
s.color('yellow','yellow')
s.right(90)
s.begin_fill()
s.circle(20)
s.end_fill()

s.left(90)
s.forward(15)
s.color('black','black')
s.right(90)
s.begin_fill()
s.circle(5)
s.end_fill()

s.penup()

s.forward(600)
