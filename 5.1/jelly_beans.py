from PIL import Image

file = Image.open("jelly_bean.png")
jbimg = file.load()

yellow_count = 0
blue_count = 0
green_count = 0
red_count = 0
pink_count = 0
brown_count = 0
purple_count = 0
black_count = 0

def is_green(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
def is_yellow(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
def is_green(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
def is_green(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
def is_green(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        r = jbimg[x, y][0]
        g = jbimg[x, y][1]
        b = jbimg[x, y][2]


