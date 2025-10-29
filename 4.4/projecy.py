import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  
  
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(72)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(72)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(72)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(72)
    drawTree(level-1, branchLength/1.7)
    
    turtle.left(72)
    drawTree(level-1, branchLength/1.7)
    turtle.back(branchLength)
  
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")
levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)

#colour