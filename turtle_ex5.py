import turtle as t
import random
import colorgram

#
# colors = colorgram.extract('image_painting.jpg', 30)
# first_color = colors[0]
# rgb = first_color.rgb
# print(rgb)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(229, 225, 221), (231, 206, 85), (218, 229, 219), (231, 222, 226), (224, 150, 89), (215, 224, 230),
              (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38),
              (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5),
              (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160),
              (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175)]

timmy = t.Turtle()
timmy.hideturtle()
timmy.speed(0)
t.colormode(255)
timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)
num_of_dots = 101

for dot_range in range(1, num_of_dots):
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)

    if dot_range % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)







screen = t.Screen()
screen.exitonclick()

