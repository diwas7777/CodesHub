# Snake Game

import turtle
import random
import time

score = 0

# screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake Game By Atharva")
screen.tracer(0)

# Snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake_pos = "None"

# apple
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)

# classes


class SnakeMovements:
  y = 0
  x = 0
  snpos = snake_pos
  
  snpos = None
	def main(self):
      if self.snpos == "up":
        self.y = snake.ycor()
        snake.sety(self.y + 15)
        
      if self.snpos == "down":
        self.y = snake.ycor()
        snake.sety(self.y - 15)
        
      if self.snpos == "right":
        self.x = snake.xcor()
        snake.setx(self.x + 15)
        
      if self.snpos == "left":
        self.x = snake.xcor()
        snake.setx(self.x - 15)
        
    def SnakeUp(self):
      self.snpos = "up"
      
    def SnakeDown(self):
      self.snpos = "down"
      
    def SnakeRight(self):
      self.snpos = "right"
      
    def SnakeLeft(self):
      self.snpos = "left"
      
instanceVar = SnakeMovements()

# Keyboard Binding

screen.listen()
screen.onkeypress(instanceVar.SnakeUp, "Up")
screen.onkeypress(instanceVar.SnakeDown, "Down")
screen.onkeypress(instanceVar.SnakeRight, "Right")
screen.onkeypress(instanceVar.SnakeLeft, "Left")

# Mainloop of the game

while True:
  if snake.distance(apple) < 20:
    score += 1
    print(score)
    applex = random.randint(-290, 290)
    appley = random.randint(-290, 290)
    apple.goto(applex, appley)
    
    time.sleep(0.1)
  
  instanceVar.main()
  screen.update()
