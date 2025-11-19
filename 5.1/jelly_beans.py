from PIL import Image\

def colour(r, g, b):
    if r>=  0 and r < 25 and g <= 255 and b >= 0 and b < 25:
        return True
    else:
        return False

file = Image.open("5.1/jelly_beans.jpg").load()
image_output = Image.open("5.1/jelly_beans.jpg")

width = image_output.width
height = image_output.height

for i in range (width):
    for j in range(height):
        r = file[i,j][0]
        g = file[i,j][1]
        b = file[i,j][2]

        if jelly_beans(r,g,b):
            image_output.putpixel((i,j), (255, 255, 255))

image_output.save("5.1/output_jelly.jpg", "jpg")