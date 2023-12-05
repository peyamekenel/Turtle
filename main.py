import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("python turttle")
turtle_instance=turtle.Turtle()

for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.right(90)

turtle_instance2=turtle.Turtle()
for i in range(5):
    turtle_instance.back(250)
    turtle_instance.left(144)

turtle_instance3=turtle.Turtle()
num_sides=8
angle=360/num_sides
side_length=100
for i in range(num_sides):
    turtle_instance.forward(side_length)
    turtle_instance.left(angle)
turtle.done()