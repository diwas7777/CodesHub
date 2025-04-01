"""Spirograph"""
import random
import turtle as t

t.colormode(255)
t.Screen().bgcolor('black')
t.Screen().title("Spirograph")
t.hideturtle()
def rcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rc = (r, g, b)
    return rc


t.pensize(2)
t.speed("fastest")


def spiro(num):
    for _ in range(int(360 / num)):
        t.color(rcolor())
        t.circle(120)
        t.setheading(t.heading() + 10)
    screen = t.Screen()
    screen.exitonclick()


spiro(4)