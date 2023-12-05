import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("python turttle")
turtle_instance=turtle.Turtle()
turtle_instance.color("yellow")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5

x=300
while x>0:
    shrinkingSquare(x)
    x=x-20
turtle.done()