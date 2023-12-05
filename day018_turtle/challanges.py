import turtle as t
import random

timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)

######## Challenge 1 - Draw a Square ############
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

########### Challenge 2 - Draw a Dashed Line ########
# for i in range(10):
#     # my solution
#     # timmy_the_turtle.forward(5)
#     # timmy_the_turtle.color("white")
#     # timmy_the_turtle.forward(5)
#     # timmy_the_turtle.color("blue")
#
#     # course solution
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()

########### Challenge 3 - Draw Shapes ########
# t.colormode(255)
# for i in range(3, 11):
#     timmy_the_turtle.color(tuple([random.randint(0, 255) for k in range(3)]))
#     for j in range(i):
#         timmy_the_turtle.forward(100)
#         turn_angle = 360/i
#         timmy_the_turtle.right(turn_angle)

########### Challenge 4 - Random walk ########
# t.colormode(255)
# directions = [0, 90, 180, 270]
# timmy_the_turtle.pensize(5)
# timmy_the_turtle.speed("fastest")
# for i in range(100):
#     timmy_the_turtle.color(tuple([random.randint(0, 255) for k in range(3)]))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.left(random.choice(directions))

########### Challenge 5 - Spirograph ########
# t.colormode(255)
# timmy_the_turtle.speed("fastest")
# for i in range(80):
#     timmy_the_turtle.color(tuple([random.randint(0, 255) for k in range(3)]))
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.left(360/80)
t.done()