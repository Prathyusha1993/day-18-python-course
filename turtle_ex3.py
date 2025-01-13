import turtle as t
from turtle import Screen
import random


timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g= random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



colours = ['forest green', 'aquamarine', 'brown', 'saddle brown', 'dark slate gray', 'hot pink', 'lime',
              'dark slate blue', 'black']
directions = [0, 90, 180, 270]
timmy.pensize(12)
timmy.speed(0)

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()