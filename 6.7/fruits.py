from PIL import Image

# List of fruit images
fruit_images = ["6.7/apple.jpg",
                "6.7/banana.jpg",
                "6.7/orange.jpg",
                "6.7/grape.jpg",
                "6.7/lemon.jpg",
                "6.7/tomato.jpg",
                "6.7/mango.jpg",
                "6.7/blueberry.jpg",
                "6.7/watermelon.jpg",
                "6.7/kiwi.jpg"]

# Get user colour
usercolour = input("What colour do you like? Red, orange, yellow, green, blue or purple? ").lower().strip()

# Colour classification function
def colours(r, g, b):
    if 230 < r <= 255 and 0 <= g < 50 and 0 <= b < 50:
        return "red"
    elif 230 < r <= 255 and 50 <= g <= 150 and 0 <= b < 50:
        return "orange"
    elif 230 < r <= 255 and 230 < g <= 255 and 0 <= b < 25:
        return "yellow"
    elif 0 <= r < 25 and 230 < g < 255 and 0 <= b < 25:
        return "green"
    elif 0 <= r < 50 and 0 <= g < 50 and 230 < b <= 255:
        return "blue"
    elif 230 < r <= 255 and 0 <= g < 50 and 230 < b <= 255:
        return "purple"
    else:
        return "other"

# Dictionary to store results
image_matches = {}
image_colours = {}

# Loop through all images
for image_path in fruit_images:
    print("------------------------------")
    print("Checking image: " + image_path)
    
    # Open and convert to RGB
    file = Image.open(image_path).convert("RGB")
    fruits = file.load()
    
    print("Image mode: " + file.mode)
    print("Image size: " + str(file.size))
    
    width = file.width
    height = file.height
    
    colour_pixels = []

    # Count pixels that match user colour
    for x in range(width):
        for y in range(height):
            Rpixel = fruits[x, y][0]
            Gpixel = fruits[x, y][1]
            Bpixel = fruits[x, y][2]

            pixel_colour = colours(Rpixel, Gpixel, Bpixel)
            if pixel_colour == usercolour:
                colour_pixels.append(fruits[x, y])
    
    # Determine dominant colour in this image
    colour_count = {}
    for x in range(width):
        for y in range(height):
            Rpixel = fruits[x, y][0]
            Gpixel = fruits[x, y][1]
            Bpixel = fruits[x, y][2]

            pixel_colour = colours(Rpixel, Gpixel, Bpixel)
            if pixel_colour in colour_count:
                colour_count[pixel_colour] += 1
            else:
                colour_count[pixel_colour] = 1

    dominant_colour = max(colour_count, key=colour_count.get)
    
    # Store results
    image_matches[image_path] = len(colour_pixels)
    image_colours[image_path] = dominant_colour
    
    print("Pixels matching user colour so far: " + str(len(colour_pixels)))
    print("Dominant colour of image: " + dominant_colour)

# Print final results
print("\nResults:")
for image_path in image_matches:
    print(image_path + ": " + str(image_matches[image_path]) + " matching pixels, dominant colour: " + image_colours[image_path])

# Find closest matching image
closest_image = max(image_matches, key=image_matches.get)
print("\nClosest matching image to your colour: " + closest_image)
