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

# Function to calculate average color
def average_color(image):
    pixels = list(image.getdata())
    total_r = total_g = total_b = 0
    count = len(pixels)
    
    for pixel in pixels:
        r, g, b = pixel[:3]
        total_r += r
        total_g += g
        total_b += b

    avg_r = total_r // count
    avg_g = total_g // count
    avg_b = total_b // count
    return (avg_r, avg_g, avg_b)

# Analyze all images
results = []
for file in fruit_images:
    img = Image.open(file)
    avg = average_color(img)
    results.append({"name": file, "rgb": avg})

# --------- DAY 2 ADDITION ---------
# Function to get user color
def get_user_color():
    color = input("Enter a color (red, green, yellow, orange, purple): ").lower()
    return color

# Function to return target RGB for basic colors
def target_color(name):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "yellow": (255, 255, 0),
        "orange": (255, 165, 0),
        "purple": (128, 0, 128)
    }
    return colors.get(name, (0, 0, 0))  # default black if unknown

# Ask the user for a color
user_color = get_user_color()
target_rgb = target_color(user_color)

print("\nTarget RGB for color", user_color.upper(), "is:", target_rgb)

# Print the analyzed fruit averages again for reference
print("\nFruit average colors:")
for r in results:
    print(r)
