import turtle
import math

t = turtle.Turtle()
t.hideturtle()
t.speed(1000)
t.width(10)
window = turtle.Screen()
window.bgcolor("black")
t.color("white")
n = 20
t.left(90)
t.penup()
t.goto(-7 * n, 0)
t.pendown()
for a in range(-7 * n, -3 * n, 1):
    x = a / n
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    t.goto(a, y * n)
for a in range(-3 * n, -1 * n - 1, 1):
    x = a / n
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    t.goto(a, y * n)

t.goto(-1 * n, 3 * n)
t.goto(int(-0.5 * n), int(2.2 * n))
t.goto(int(0.5 * n), int(2.2 * n))
t.goto(1 * n, 3 * n)
for a in range(1 * n + 1, 3 * n + 1, 1):
    x = a / n
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    t.goto(a, y * n)
for a in range(3 * n + 1, 7 * n + 1, 1):
    x = a / n
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    t.goto(a, y * n)

for a in range(7 * n, 4 * n, -1):
    x = a / n
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    t.goto(a, y * n)

for a in range(4 * n, -4 * n, -1):
    x = a / n
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    t.goto(a, y * n)

for a in range(-4 * n - 1, -7 * n - 1, -1):
    x = a / n
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    t.goto(a, y * n)

t.penup()

t.goto(300, 300)
turtle.done()
