#Fidget spinner game

from turtle import *
state = {'turn':0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(115, 'red')
    back(105)
    right(125)
    forward(105)
    dot(125, 'greenery')
    back(110)
    right(125)
    forward(105)
    dot(125, 'blue')
    back(105)
    right(120)
    update()
def animate(): #animated
    if state['turn']>0:
        state['turn']-=1

        spinner()
        ontimer(animate,20)
def flick():
    state['turn']+=10

setup(440, 440, 380, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()