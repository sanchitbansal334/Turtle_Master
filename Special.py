import turtle
from random import randint
'''spiral_3d,
chakra,
rose,
fractal_tree
mandala,
shell_art,
Spiral_Art'''
def spiral_3d():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	t=turtle.Turtle()
	x=1
	t.speed(0)
	t.shape("turtle")

	while x<400:
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		turtle.colormode(255)
		t.color(r,g,b)
		t.forward(5+x)
		t.right(91)
		x=x+1
	t.hideturtle()
def chakra():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	t=turtle.Turtle()
	t.pencolor('blue')
	t.speed(0)
	c=0
	while True:
		for i in range(4):
			t.forward(80)
			t.right(90)
		t.right(5)
		c+=1
		if c>=360/5:
			break
	t.hideturtle()
def Rose():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	def curve(x) :
	    for i in range(90):
	        x.right(1)
	        x.forward(1)

	#flower
	a=turtle.Turtle()
	a.color("red")
	a.speed(0)
	a.pensize(2)
	a.begin_fill()
	a.left(180)
	curve(a)
	a.forward(100)
	a.right(135)
	a.forward(50)
	a.left(90)
	a.forward(50)
	a.right(90)
	a.forward(50)
	a.left(90)
	a.forward(50)
	a.right(135)
	a.forward(100)
	curve(a)
	a.forward(25)
	a.end_fill()
	a.hideturtle()

	#stem
	b = turtle.Turtle()
	b.color("green")
	b.pensize(2)
	b.begin_fill()
	b.forward(15)
	b.right(90)
	b.forward(300)
	b.right(90)
	b.forward(15)
	b.right(90)
	b.forward(300)
	b.end_fill()
	b.hideturtle()

	#leaf
	c = turtle.Turtle()
	c.color("green")
	c.pensize(2)
	c.begin_fill()
	c.forward(15)
	c.right(90)
	c.forward(120)
	c.left(120)
	c.forward(30)
	c.left(45)
	for i in range(90):
	    c.forward(1)
	    c.right(1)
	c.right(90)
	for i in range(90):
	    c.forward(1)
	    c.right(1)
	c.left(45)
	c.forward(30)
	c.end_fill()
	c.hideturtle()
def fractal_tree():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	x = turtle.Turtle()
	x.left(90)
	x.speed(20)
	x.color('white')
	x.pensize(5)
	def Draw_Tree(a):
		if a<10:
			return
		else :
			x.forward(a)
			x.left(30)
			Draw_Tree(3*a/4)
			x.right(60)
			Draw_Tree(3*a/4)
			x.left(30)
			x.backward(a)
	Draw_Tree(80)
	x.hideturtle()
def mandala():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	man = turtle.Turtle()
	man.pensize(2)
	man.speed(20)
	for i in range (6):
		for colour in ["red" , "white" , "blue" , "green" , "magenta" , "yellow"]:
			man.color(colour)
			man.circle(100)
			man.left(10)
	man.hideturtle()
def shell_art():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	t = turtle.Turtle()
	t.color("green")
	t.hideturtle()
	t.speed(0)
	for i in range(100):
		t.circle(i*2)
		t._rotate(5)
def spiral_art():
	turtle.clearscreen()
	window = turtle.Screen()
	window.bgcolor("black")
	window.title("Turtle Master")
	colors = ["red", "yellow" , "green" , "purple" , "blue" , "orange"]
	t = turtle.Pen()
	t.speed(10)
	for x in range (200):
	    t.pencolor(colors[x%6])
	    t.width(x/100+1)
	    t.forward(x)
	    t.left(59)
	t.hideturtle()
