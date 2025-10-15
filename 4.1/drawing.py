"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""

import turtle
smeg = turtle.Turtle()

while True:
    command = input("What shall I do? ")

    if command == "stop":
        break

    if command == "l":
        smeg.left(45)
        smeg.forward(50)

    if command == "r":
        smeg.right(45)
        smeg.forward(50)

    if command == "f":
        smeg.forward(50)

    if command == "c":
        smeg.circle(67)
        