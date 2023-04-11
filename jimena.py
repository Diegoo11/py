import turtle

#Procedimiento para crear el cuadrado
windows = turtle.Screen()
windows.bgcolor('yellow')

#Letras BINGO  ------------------------------------------
lether1 = turtle.Turtle()
lether1.penup()
lether1.goto(-200 - 36, 200- 36)
lether1.pendown()
lether1.color("red")
lether1.write("B", move=False, font=('Arial', 70, "bold"))

lether2 = turtle.Turtle()
lether2.penup()
lether2.goto(-80- 36, 200- 36)
lether2.pendown()
lether2.color("blue")
lether2.write("I", move=False, font=('Arial', 70, "bold"))

lether3 = turtle.Turtle()
lether3.penup()
lether3.goto(0- 36, 200- 36)
lether3.pendown()
lether3.color("purple")
lether3.write("N", move=False, font=('Arial', 70, "bold"))

lether4 = turtle.Turtle()
lether4.penup()
lether4.goto(100- 36, 200- 36)
lether4.pendown()
lether4.color("green")
lether4.write("G", move=False, font=('Arial', 70, "bold"))

lether5 = turtle.Turtle()
lether5.penup()
lether5.goto(200- 36, 200- 36)
lether5.pendown()
lether5.color("orange")
lether5.write("O", move=False, font=('Arial', 70, "bold"))


#cuadrados BlANCOS 76x76 ------------------------------------------
positionsSquare = [[-200, 100, 17], [-100, 100, 17], [0, 100, 17], [100, 100, 17], [200, 100, 17],
    [-200, 0, 17], [-100, 0, 17], [0, 0, 17], [100, 0, 17], [200, 0, 17],
    [-200, -100, 17], [-100, -100, 17], [0, -100, 17], [100, -100, 17], [200, -100, 17],
    [-200, -200, 17], [-100, -200, 17], [0, -200, 17], [100, -200, 17], [200, -200, 17],
    [-200, -300, 17], [-100, -300, 17], [0, -300, 17], [100, -300, 17], [200, -300, 17],
]

def generator_square(var_one, var_two): #funcion creadora de cuadrados
    square = turtle.Turtle()
    square.color("white")
    square.fillcolor("white")
    square.penup()
    square.goto(var_one, var_two)
    square.begin_fill()
    square.forward(38)
    square.pendown()
    square.left(90)
    square.forward(38)
    square.left(90)
    square.forward(76)
    square.left(90)
    square.forward(76)
    square.left(90)
    square.forward(76)
    square.left(90)
    square.forward(38)
    square.end_fill()

for positionArray in positionsSquare:
    generator_square(positionArray[0], positionArray[1])
    print(positionArray[0])

#numero del BINGO ------------------------------------------
def generator_numbers(coord_x, coord_y, num): #funcion creadora de cuadrados
    number = turtle.Turtle()
    number.color("black")
    #number.fillcolor("black")
    number.penup()
    number.goto(coord_x-36, coord_y-36)
    #number.begin_fill()
    #number.forward(38)
    number.pendown()
    number.write(num, move=False, font=('Arial', 50, "bold"))
    #number.end_fill()

for numbersInSquare in positionsSquare:
    generator_numbers(numbersInSquare[0], numbersInSquare[1], numbersInSquare[2])

turtle.done()
