from turtle import Turtle, Screen
import turtle as t
import random

# Set up turtle parameters
turtle = Turtle()
turtle.shape("turtle")
turtle.color('green')

# Enable RGB color mode
t.colormode(255)


# Generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

# Possible directions for the turtle
directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed(0)

# Generate a random walk
for _ in range(1000):
    direction = random.choice(directions)
    turtle.pencolor(random_color())

    turtle.forward(30)
    turtle.setheading(direction)

# Close the window on click
screen = Screen()
screen.exitonclick()
