from PIL import Image

# List of fruit images
fruit_images = [
    "6.7/apple.jpg",
    "6.7/banana.jpg",
    "6.7/orange.jpg",
    "6.7/grape.jpg",
    "6.7/lemon.jpg",
    "6.7/tomato.jpg",
    "6.7/mango.jpg",
    "6.7/blueberry.jpg",
    "6.7/watermelon.jpg",
    "6.7/kiwi.jpg"
]

# Ask user for favourite colour
usercolour = input(
    "What colour do you like? Red, orange, yellow, green, blue or purple? "
).lower().strip()

# Function to classify pixel colour
def colours(r, g, b):
    if 160 < r <= 200 and g < 20 and b < 55:
        return "red"
    elif 230 < r <= 255 and 50 <= g <= 150 and b < 50:
        return "orange"
    elif 230 < r <= 250 and 190 < g <= 220 and b < 20:
        return "yellow"
    elif r < 210 and 170 < g <= 245 and b < 90:
        return "green"
    elif r < 80 and g < 100 and 110 < b <= 130:
        return "blue"
    elif 150 < r <= 220 and 110 < g <= 160 and 150 < b <= 220:
        return "purple"
    else:
        return "other"

# Dictionaries to store results
image_matches = {}
image_colours = {}

# Loop through images
for image_path in fruit_images:
    print("------------------------------")
    print("Checking image:", image_path)

    # Open image and make it smaller (simple method)
    # Open the image file
    image = Image.open(image_path)

    # Load the pixel data
    pixels = image.load()
    image = image.resize((50, 50))   # <-- SIMPLE resize added here

    pixels = image.load()
    width, height = image.size

    user_colour_count = 0
    colour_count = {}

    # Check every pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixel_colour = colours(r, g, b)

            # Count user's chosen colour
            if pixel_colour == usercolour:
                user_colour_count += 1

            # Count all colours
            if pixel_colour in colour_count:
                colour_count[pixel_colour] += 1
            else:
                colour_count[pixel_colour] = 1

    # Find dominant colour
    dominant_colour = None
    max_count = 0

    for colour in colour_count:
        count = colour_count[colour]
        if count > max_count:
            max_count = count
            dominant_colour = colour

    # Store results
    image_matches[image_path] = user_colour_count
    image_colours[image_path] = dominant_colour

    print("Matching pixels:", user_colour_count)
    print("Dominant colour:", dominant_colour)

# Show final results
print("\nFinal Results:")
for image_path in image_matches:
    print(
        image_path,
        "-",
        image_matches[image_path],
        "matching pixels, dominant colour:",
        image_colours[image_path]
    )

# Find closest matching image
# Find top 2 matching images
top_two = sorted(image_matches, key=image_matches.get, reverse=True)[:2]

"6.7/apple.jpg" == "apples"
for image_path in top_two:
    print("Your favourite fruits determined by your favourite colour are " + image_path)


