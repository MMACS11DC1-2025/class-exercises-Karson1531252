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

def colours(r, g, b):
    if 230 < r <= 255 and 0 <= g < 25 and 0 <= b < 25:
        return "red"
    
    elif 230 < r <= 255 and 0 <= g < 25 and 0 <= b < 25:
        return "orange"
    
    elif 230 < r <= 255 and 230 < g <= 255 and 0 <= b < 25:
        return "yellow"
    
    elif 230 < r <= 255 and 0 <= g < 25 and 0 <= b < 25:
        return "green"
    
    elif 230 < r <= 255 and 0 <= g < 25 and 0 <= b < 25:
        return "blue"
    
    elif 230 < r <= 255 and 0 <= g < 25 and 0 <= b < 25:
        return "purple"
print(usercolour, red)
