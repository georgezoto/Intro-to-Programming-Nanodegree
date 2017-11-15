import turtle

def initialize_turtle(shape, color1, color2, speed):
    little_turtle = turtle.Turtle()
    little_turtle.shape(shape)
    little_turtle.color(color1, color2)
    little_turtle.speed(speed)
    return little_turtle

def draw_square(little_turtle):
    for turn in range(0,4):
        little_turtle.forward(100)
        little_turtle.right(90)

def draw_triangle(turtle):
    for turn in range(0,3):
        turtle.forward(100)
        turtle.right(120)

def draw_circle_of_squares():
    window = turtle.Screen()
    window.bgcolor('red')

    little_turtle = initialize_turtle('turtle', 'yellow', 'green', 0)

    for turn in range(0,36):
        draw_triangle(little_turtle)
        little_turtle.right(10)

    small_turtle = initialize_turtle('turtle', 'blue', 'white', 0)
    small_turtle.circle(100)

    window.exitonclick()

draw_circle_of_squares()
