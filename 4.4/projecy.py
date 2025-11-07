import turtle

# Settings for fractal colours and defaults
SETTINGS = {
    "colours": ["red", "blue", "green", "purple", "orange"],  # Colours to choose from
    "default": {"branch_length": 120, "levels": 3}  # Default branch length and recursion levels
}

# Function to draw fractal triangle and count how many times it runs
def draw_tree(level, branch_length):
    calls = 1  # Count this function call
    if level > 0:  # Stop when level is 0
        turtle.color(colour)  # Set drawing colour
        turtle.forward(branch_length)
        turtle.left(120)
        calls += draw_tree(level-1, branch_length/1.7)
        
        turtle.left(120)
        calls += draw_tree(level-1, branch_length/1.7)
        
        turtle.left(120)
        calls += draw_tree(level-1, branch_length/1.7)
        turtle.back(branch_length)  # Go back to previous position
    return calls  # Return total number of calls

# Start of program
print("Fractal Art Generator")  # Program title

# Get user inputs
x = int(input("Start X (default 0): ") or 0)  # Starting X position
y = int(input("Start Y (default 0): ") or -180)  # Starting Y position
levels = int(input("Levels (default 3): ") or SETTINGS["default"]["levels"])  # How many recursion levels
colour = input("Colour (red, blue, green, purple, orange): ").lower() or "red"  # Pick colour

# Check if the colour is valid
if colour not in SETTINGS["colours"]:
    colour = "red"  # Use red if input is invalid

# Create screen
screen = turtle.Screen()

# Simple background colour matching
if colour == "red":
    screen.bgcolor("mistyrose")
elif colour == "blue":
    screen.bgcolor("lightcyan")
elif colour == "green":
    screen.bgcolor("honeydew")
elif colour == "purple":
    screen.bgcolor("lavender")
elif colour == "orange":
    screen.bgcolor("moccasin")
else:
    screen.bgcolor("white")  # Default

# Set up turtle
turtle = turtle.Turtle()  # Create turtle
turtle.speed(10)  # Fastest drawing
turtle.penup()  # Lift pen to move
turtle.goto(x, y)  # Move to starting position
turtle.left(90)  # Face up
turtle.pendown()  # Put pen down to draw
turtle.width(2)  # Line thickness

# Draw fractal and show total calls
total_calls = draw_tree(levels, SETTINGS["default"]["branch_length"])
print("Fractal complete! Total calls:", total_calls)

turtle.done()  # Finish drawing
