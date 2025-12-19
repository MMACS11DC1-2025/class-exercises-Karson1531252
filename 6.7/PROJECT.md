# Fruit Colour Analysis Project

## Project Overview
This project looks at a set of fruit images and finds which ones match the user’s favourite colour the most. It counts the number of pixels in each image that match the chosen colour and shows the top matching images. The images used are: apple, banana, orange, grape, lemon, tomato, mango, blueberry, watermelon, and kiwi.

## Visual Feature
The program detects **colour density**. Each pixel is checked to see if it matches red, orange, yellow, green, blue, or purple. Pixels that match the chosen colour increase the image's score. This works well because fruit colours are mostly consistent.

## Testing
- Functions were tested individually to make sure they work.  
- The `colours()` function was checked by printing the main colour of each fruit.  
- Different favourite colours were tested to see if results made sense.  
- Edge cases were tested to make sure the program doesn’t crash.

## Performance
The program measures how long it takes to process all images using the `time` module. Images are resized to 50×50 pixels to make processing faster while keeping results accurate. Example output:  


## Challenges
1. Choosing RGB ranges for each colour. Solution: Tested many images and adjusted ranges.  
2. Making the program faster. Solution: Resized images before counting pixels.  
3. Sorting and searching manually. Solution: Used Selection Sort and Binary Search on the master list.

## Notes
- Images are sorted by colour match using **Selection Sort**.  
- The program can find a specific score using **Binary Search**.  
- Variable names and functions are clear and easy to understand.
