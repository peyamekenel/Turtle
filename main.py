import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("python turttle")
turtle_instance=turtle.Turtle()

for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.right(90)
turtle.done()
