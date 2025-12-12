from PIL import Image
#use colour picker

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

usercolour = input("What colour do you like? Red, orange , yellow, green, blue or purple?")
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


