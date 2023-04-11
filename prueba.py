import turtle

#Procedimiento para crear el cuadrado
windows = turtle.Screen()
windows.bgcolor('yellow')

t1 = turtle.Turtle()
#t1.penup()
t1.goto(200, 200)
t1.left(90)
t1.forward(100)
t1.circle(50)

t2 = turtle.Turtle()
t2.penup()
t2.goto(-200, 200)
t2.pendown()
t2.write("BINGO", move=False, font=('Arial', 24, "bold"))

pen3 = turtle.Turtle()
pen3.fillcolor((0, 0, 0))
pen3.begin_fill()
pen3.circle(100)
pen3.end_fill()




turtle.done()
