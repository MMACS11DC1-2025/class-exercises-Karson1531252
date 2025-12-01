from PIL import Image

# List of fruit images
fruit_images = ["6.7/apple.jpg", "6.7/banana.jpg", "6.7/orange.jpg", "6.7/grape.jpg", "6.7/lemon.jpg", "6.7/tomato.jpg", "6.7/mango.jpg", "6.7/blueberry.jpg", "6.7/watermelon.jpg", "6.7/kiwi,jpg"]

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

# Print results
for r in results:
    print(r)
