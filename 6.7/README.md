Project Overview

This project analyzes fruit images by looking at pixel colours. The program compares images based on how much they match the user’s favourite colour.

Theme

The theme of this project is fruit images. Fruits are easy to identify using colour, which makes them good for image analysis.

Visual Feature

The visual feature being detected is colour density. The program counts how many pixels match a specific colour chosen by the user.

How the Feature Is Detected

Each pixel’s RGB values are checked against colour ranges. If a pixel fits the range for a colour (like red or yellow), it is counted. The more matching pixels an image has, the higher its score.

Image Processing

Each image is resized to 50×50 pixels to make the program faster. The program then loops through every pixel and checks its colour.

Feature Density Score

The Feature Density Score is the number of pixels in an image that match the user’s chosen colour.

Sorting the Results

The images are sorted using Selection Sort, from highest score to lowest score. The top 5 matching images are shown.

Searching

A Binary Search is used to find an image with a specific feature score in the sorted list.

Code Profiling

The time module measures how long the program takes to process all images. The time is printed to three decimal places.

Testing

The program was tested by running it with different colours and checking if the results made sense for each fruit.

Challenges Faced

Choosing accurate RGB ranges was challenging. This was solved by adjusting the values and testing with multiple images.

Performance Notes

Resizing images greatly reduced processing time while keeping results accurate.
