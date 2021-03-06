import turtle
def square():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	sq=turtle.Turtle()
	sq.speed(5)
	sq.color("cyan")
	sq.pensize(3)
	for i in range(4):
		sq.forward(100)
		sq.left(90)
	sq.hideturtle()
def triangle():
    turtle.clearscreen()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    tr=turtle.Turtle()
    tr.speed(5)
    tr.color("lime")
    tr.pensize(2)
    for i in range(3):
        tr.forward(100)
        tr.left(120)
    tr.hideturtle()
def star():
    turtle.clearscreen()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    st=turtle.Turtle()
    st.speed(5)
    st.color("yellow")
    st.pensize(2)
    st.up()
    st.backward(75)
    st.left(90)
    st.forward(100)
    st.right(90)
    st.down()
    for i in range(5):
        st.forward(150)
        st.right(144)
    st.hideturtle()
def heart():
    def curve(x) :
        for i in range(200):
            x.right(1)
            x.forward(1)

    turtle.clearscreen()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    a = turtle.Turtle()
    a.pensize(3)
    a.speed(30)
    a.color("red" , "pink")
    '''a.up()
    a.right(90)
    a.forward(200)
    a.left(90)
    a.down()'''
    a.begin_fill()
    a.left(140)
    a.forward(111.65)
    curve(a)

    a.left(120)
    curve(a)
    a.forward(111.65)
    a.end_fill()
    a.hideturtle()
#rhombus
#diamond
def circle():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	ci=turtle.Turtle()
	ci.speed(5)
	ci.color("cyan")
	ci.pensize(3)
	ci.up()
	ci.right(90)
	ci.forward(50)
	ci.left(90)
	ci.down()
	ci.circle(100)
	ci.hideturtle()

def ellipse():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	el=turtle.Turtle()
	el.speed(5)
	el.color("orange")
	el.pensize(3)
	el.up()
	el.backward(100)
	el.down()
	el.right(45)
	for loop in range(2):
		el.circle(200,90)
		el.circle(200/2,90)
	el.hideturtle()
def rectangle():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	re=turtle.Turtle()
	re.speed(5)
	re.color("yellow")
	re.pensize(3)
	re.up()
	re.backward(100)
	re.down()
	re.forward(200)
	re.left(90)
	re.forward(100)
	re.left(90)
	re.forward(200)
	re.left(90)
	re.forward(100)
	re.left(90)
	re.hideturtle()
def rhombus():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	rh=turtle.Turtle()
	rh.speed(5)
	rh.color("aqua")
	rh.pensize(3)
	rh.up()
	rh.backward(50)
	rh.down()
	rh.forward(100)
	rh.left(60)
	rh.forward(100)
	rh.left(120)
	rh.forward(100)
	rh.left(60)
	rh.forward(100)
	rh.left(120)
	rh.hideturtle()

def polygon(number):
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	po=turtle.Turtle()
	po.speed(5)
	po.color("aqua")
	po.pensize(3)
	exteriorAngle=360/number
	length=600/number
	po.penup()
	po.goto(-length/2,-length/2)
	po.pendown()
	for i in range(0,number):
		po.forward(length)
		po.left(exteriorAngle)
	po.hideturtle()