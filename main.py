import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("python turttle")
turtle_instance=turtle.Turtle()
turtle_instance.color("yellow")
turtle.speed(0)
colors_List= ["red","blue","pink","green","orange","brown"]
for i in range(20):
    turtle_instance.color(colors_List[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)
turtle.mainloop()
