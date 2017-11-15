import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    little_turtle = turtle.Turtle()
    little_turtle.shape('turtle')
    little_turtle.color("green", "yellow")
    little_turtle.speed(2)

    for turn in range(0,4):
        little_turtle.forward(100)
        little_turtle.right(90)

    small_turtle = turtle.Turtle()
    small_turtle.shape('turtle')
    small_turtle.color("white", "blue")
    small_turtle.speed(2)
    small_turtle.circle(100)

    window.exitonclick()

draw_square()
