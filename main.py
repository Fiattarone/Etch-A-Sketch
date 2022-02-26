from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.speed("fastest")
my_turtle.width(4)
screen = Screen()

def move_forward():
    my_turtle.forward(10)


def move_right():
    my_turtle.right(10)


def move_left():
    my_turtle.left(10)


def move_backward():
    my_turtle.backward(10)


def screen_clear():
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
    my_turtle.clear()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="c", fun=screen_clear)
# screen.onkeypress(key="space",fun=move_forward)
screen.exitonclick()