from PIL import Image

file = Image.open("5.1/output_jelly.jpg")
jbimg = file.load()

yellow_count = 0
blue_count = 0
green_count = 0
red_count = 0
purple_count = 0

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        r = jbimg[x, y][0]
        g = jbimg[x, y][1]
        b = jbimg[x, y][2]

        # red
        if 165 <= r >= 190 and 0 <= g >= 15 and 0 <= b >= 15:
            red_count += 1
        # purple
        if 55 <= r >= 75 and 55 <= g >= 85 and 175 <= b >= 215:
            purple_count += 1
        # blue
        if 0 <= r >= 15 and 23 <= g >= 35 and 90 <= b >= 120:
            blue_count += 1
        # yellow
        if 150 <= r <= 255 and 150 <= g <= 255 and 0 <= b <= 150:
            yellow_count += 1
        # green
        if 100 <= r >= 120 and 40 <= g >= 75 and 20 <= b >= 45:
            green_count += 1

percent_yellow = 100*yellow_count/(width*height)
percent_red = 100*red_count/(width*height)
percent_blue = 100*blue_count/(width*height)
percent_purple = 100*purple_count/(width*height)
percent_green = 100*green_count/(width*height)

print(percent-green)
