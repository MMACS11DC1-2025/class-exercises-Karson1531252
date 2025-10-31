
import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  
  
  if level > 0:
    turtle.color("red")
    turtle.forward(branchLength)
    turtle.left(120)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(120)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(120)
    drawTree(level-1, branchLength/1.7)
    turtle.back(branchLength)
  
  if level > 1:
    turtle.color("blue")
    
    
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("red")
turtle.width(3)
turtle.shape("triangle")
levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)