from PIL import Image
def is_green(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range (width):
    for j in range(height):
        r = image_green[i,j][0]
        g = image_green[i,j][1]
        b = image_green[i,j][2]

        if coolcolours.is_green(r,g,b):
            beach_colour = image_beach[i,j]
            image_output.putpixel((i,j), beach_colour)

image_output.save("5.1/output.png", "png")