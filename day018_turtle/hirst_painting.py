from turtle import *

import colorgram
import random


colors = colorgram.extract('image.jpg', 10)
# color_list = []
# for i in range(10):
#     rgb_obj = colors[i].rgb
#     color = (rgb_obj.r, rgb_obj.g, rgb_obj.b)
#     color_list.append(color)
color_list = [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(10)]

# remove white
color_list = color_list[1:]

t = Turtle()
colormode(255)
print(t.position())
t.penup()
start_x = -300
start_y = -300
t.goto(start_x, start_y)
for i in range(10):
    for j in range(10):
        t.pendown()
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
    start_y += 50
    t.goto(start_x, start_y)
done()


