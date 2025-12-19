# Image Explorer Project – Fruit Colour Analysis

## Project Overview
This project analyzes a set of fruit images to determine which fruits best match a user's favourite colour.
The theme is fruit imagery, and the program scans pixel data to measure colour density.

## Visual Feature
The detected feature is dominant colour density.
Each pixel is classified using RGB thresholds, allowing the program to count how many pixels match the user's chosen colour.

This approach works because fruits tend to have strong, consistent colour regions that can be detected using RGB ranges.

## Feature Detection Justification
Colour-based detection is commonly used in computer vision tasks such as:
- Food recognition
- Agricultural quality control
- Image segmentation

RGB thresholding is effective for simple datasets with strong colour contrasts.

## Testing & Validation
- Tested individual images to confirm dominant colour accuracy
- Verified that selection sort orders images correctly
- Confirmed binary search finds valid scores
- Reduced image size to improve performance

## Code Profiling
The program measures pixel-processing time using the `time` module.
Example output:
