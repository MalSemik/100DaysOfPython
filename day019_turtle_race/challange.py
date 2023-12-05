from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.forward(-10)


def rotate_clockwise():
    t.right(5)


def rotate_counter_clockwise():
    t.left(5)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_counter_clockwise)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
