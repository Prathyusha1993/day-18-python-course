from turtle import Turtle, Screen
import random


timmy = Turtle()
# steps = 100
# step_size = 20

# this is my answer

# def random_walk(tim, steps, step_size):
#     colors = ['blue', 'forest green', 'aquamarine', 'brown', 'saddle brown', 'dark slate gray', 'hot pink', 'lime',
#               'dark slate blue', 'black']
#     for _ in range(steps):
#         tim.pensize(10)
#         tim.forward(step_size)
#         tim.left(random.choice([0, 90, 20, 13, 120, 100]))
#         tim.color(random.choice(colors))
#
#
# random_walk(timmy, steps, step_size)




# lecture answer for random walk:
colours = ['forest green', 'aquamarine', 'brown', 'saddle brown', 'dark slate gray', 'hot pink', 'lime',
              'dark slate blue', 'black']
directions = [0, 90, 180, 270]
timmy.pensize(12)
timmy.speed(0)

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))





screen = Screen()
screen.exitonclick()