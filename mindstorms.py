import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)


def draw_art():
	window=turtle.Screen()
	window.bgcolor("red")
	#Creating the turtle
	brad=turtle.Turtle()
	brad.shape('turtle')
	brad.speed(2)
	brad.color('yellow')

	draw_square(brad)


	# angie=turtle.Turtle()
	# angie.shape("arrow")
	# angie.color("blue")
	# angie.circle(50)


	window.exitonclick()


	
draw_art()
