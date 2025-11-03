import turtle

#Fractal settings with available colours and defaults
SETTINGS = {
    "colours": ["red", "blue", "green", "purple", "orange"],  #Colours user can pick
    "default": {"branch_length": 120, "levels": 3}  #Default branch length and recursion levels
}

#Recursive function to draw fractal triangle and count calls
def draw_tree(t, level, branch_length, colour):
    calls = 1  #Count this recursive call
    if level > 0:  #Stop recursion at level 0
        t.color(colour)  #Set the turtle drawing colour
        for _ in range(3):  #Draw three sides of the triangle
            t.forward(branch_length)  # Draw one side
            t.left(120)  #Turn 120 degrees to next corner
            calls += draw_tree(t, level - 1, branch_length / 1.7, colour)  #Recurse with smaller branch
        t.back(branch_length)  #Go back to starting position
    return calls  #Return total calls including this one

#Main program starts here
print("Fractal Art Generator")  #Show title to user

#Get user inputs for position, levels, and colour
x = int(input("Start X (default 0): ") or 0)  #X coordinate to start
y = int(input("Start Y (default 0): ") or 0)  #Y coordinate to start
levels = int(input("Levels (default 3): ") or SETTINGS["default"]["levels"])  #How many recursion levels
colour = input("Colour (red, blue, green, purple, orange): ") or "red"  #Pick colour

#Check if colour is valid
if colour not in SETTINGS["colours"]:
    colour = "red"  #Use red if invalid colour given

#Set up the turtle for drawing
t = turtle.Turtle()  #Create turtle object
t.speed(0)  #Set drawing speed to fastest
t.penup()  #Lift pen to move to start
t.goto(x, y) #Move to starting position
t.left(90)  #Face upwards
t.pendown()  #Start drawing
t.width(2)  #Set line thickness

#Draw fractal and show total recursive calls
print("Fractal complete! Total calls:", draw_tree(t, levels, SETTINGS["default"]["branch_length"], colour))

turtle.done()  #Finish drawing

#Documentation
#Project Overview:
#This program generates a simple recursive triangle fractal using Python's turtle module.
#Users can choose starting coordinates, recursion levels, and line colour.

#Recursive Approach:
#The function draw_tree() calls itself three times per level to draw smaller triangles.
#Base case is when level <= 0, which stops further recursion.
#Branch length decreases by dividing by 1.7 each recursive call.

#User Inputs:
#x, y: Starting position of the fractal on the screen.
#levels: Number of recursion levels (integer >=1 recommended)
#colour: Line colour from the available list.

#Test Cases:
#1)x=0, y=0, levels=2, colour='red'
#  Expected: Small triangle fractal at center, 7 recursive calls.
#2)x=-100, y=-100, levels=3, colour='blue'
#  Expected: Larger fractal shifted to bottom-left, 22 recursive calls.

#Reasonable Recursion Depth:
#Too low (1-2): fractal is very simple and not visually interesting.
#Too high (6+): may slow down drawing and clutter the screen.

#Debugging Notes:
#Ensure branch_length > 0 to avoid turtle errors.
#Colour validation prevents invalid colour strings.
#Recursive call counting helps verify recursion works correctly.
