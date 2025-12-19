<<<<<<< HEAD
from PIL import Image
import time
=======
# Favourite fruit calc
# Author: Karson Lum
# Date : Dec 19, 2025
>>>>>>> e0199c7 (j final)

from PIL import Image
import time   # <-- ADDED for profiling

# LIST OF IMAGES 
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

# USER INPUT
usercolour = input(
    "What colour do you like? Red, orange, yellow, green, blue or purple? "
).lower().strip()

<<<<<<< HEAD
# Check what colour a pixel is
=======
# Colour Data
>>>>>>> e0199c7 (j final)
def colours(r, g, b):
    """
    Determines the colour category of a pixel.
    This is the visual feature detector.
    """
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

# Boolean feature checker
def is_target_feature(r, g, b, target_colour):
    """
    Returns True if pixel matches the user's chosen colour.
    """
    return colours(r, g, b) == target_colour

# DATA STRUCTURES
image_matches = {}
image_colours = {}
master_list = []

# Master list for sorting & searching
feature_scores = []  

# START TIMING
start_time = time.time()

# IMAGE PROCESSING LOOP
for image_path in fruit_images:
    print("\nChecking image:", image_path)

    image = Image.open(image_path)
    image = image.resize((50, 50))  # resize the image to make the code faster
    pixels = image.load()
    width, height = image.size

    user_colour_count = 0
    colour_count = {}

    # NESTED PIXEL ITERATION
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

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

    # APPEND TO MASTER LIST
    feature_scores.append((image_path, user_colour_count))

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

sorted_scores = selection_sort(feature_scores)

# Output top 5 results
print("\nTop 5 Images by Feature Density:")
for item in sorted_scores[:5]:
    print(item)

# BINARY SEARCH
def binary_search(sorted_list, target_score):
    """
    Searches for a specific feature score using Binary Search.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid][1] == target_score:
            return sorted_list[mid]
        elif sorted_list[mid][1] < target_score:
            high = mid - 1
        else:
            low = mid + 1

    return None


# Example binary search usage
search_score = sorted_scores[0][1]
result = binary_search(sorted_scores, search_score)

print("\nBinary Search Result:", result)

# FINAL USER OUTPUT
top_two = sorted_scores[:2]
for image_path, score in top_two:
    print("Your favourite fruits determined by your favourite colour are", image_path)
