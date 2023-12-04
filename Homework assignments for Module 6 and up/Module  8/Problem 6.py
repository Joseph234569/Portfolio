import turtle

def draw_polygon(sides, length):
    angle = 180 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

# Set up the turtle screen


alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()