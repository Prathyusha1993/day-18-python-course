from turtle import Turtle, Screen
import random


timmy = Turtle()

# another example
colors = ['blue', 'forest green', 'aquamarine', 'brown', 'saddle brown',  'dark slate gray', 'hot pink', 'lime', 'dark slate blue', 'black']
def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shapes_num in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shapes(shapes_num)

# draw_shapes(3)
# draw_shapes(4)
# draw_shapes(5)
# draw_shapes(6)
# draw_shapes(7)
# draw_shapes(8)
# draw_shapes(9)
# draw_shapes(10)