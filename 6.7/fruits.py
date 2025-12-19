from PIL import Image
import time

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

# Check what colour a pixel is
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

# Store results
image_matches = {}
image_colours = {}
master_list = []

# Start timing
start_time = time.time()

# Go through each image
for image_path in fruit_images:
    print("\n")
    print("Checking image:", image_path)

    image = Image.open(image_path)

    # Make image smaller
    image = image.resize((50, 50))
    pixels = image.load()
    width, height = image.size

    user_colour_count = 0
    colour_count = {}

    # Check every pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixel_colour = colours(r, g, b)

            if pixel_colour == usercolour:
                user_colour_count += 1

            if pixel_colour in colour_count:
                colour_count[pixel_colour] += 1
            else:
                colour_count[pixel_colour] = 1

    # Find most common colour
    dominant_colour = None
    max_count = 0
    for colour in colour_count:
        if colour_count[colour] > max_count:
            max_count = colour_count[colour]
            dominant_colour = colour

    image_matches[image_path] = user_colour_count
    image_colours[image_path] = dominant_colour
    master_list.append([image_path, user_colour_count])

    print("Matching pixels:", user_colour_count)
    print("Dominant colour:", dominant_colour)

# Stop timing
end_time = time.time()
elapsed_time = end_time - start_time
rounded_time = str(round(elapsed_time, 3))
print("\nPixel processing time: " + rounded_time + " seconds")

# Sort results
def selection_sort(data):
    for i in range(len(data)):
        max_index = i
        for j in range(i + 1, len(data)):
            if data[j][1] > data[max_index][1]:
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]

selection_sort(master_list)

# Show top 5 images
print("\nTop 5 images:")
for item in master_list[:5]:
    print(item[0], "-", item[1], "matching pixels")

# Search for a score
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][1] == target:
            return data[mid]
        elif data[mid][1] < target:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Example search
search_value = master_list[0][1]
result = binary_search(master_list, search_value)

if result:
    print("\nBinary search found:", result[0], "with score", result[1])
