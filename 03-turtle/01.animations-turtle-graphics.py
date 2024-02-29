import turtle 
turtle.bgcolor ("black")
turtle.pensize(5)
turtle.speed(0.1)
colours = ["green","yellow","blue"]
for i in range(20):
    for color in colours:
        turtle.color(color)
        turtle.circle(128)
        turtle.right(10)


turtle.mainloop