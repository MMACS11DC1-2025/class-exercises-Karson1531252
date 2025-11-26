# Documentation
# Project Overview:
# This program generates a simple recursive triangle fractal using Python's turtle module.
# Users can choose starting coordinates, recursion levels, and line colour.

# Recursive Approach:
# The function draw_tree() calls itself three times per level to draw smaller triangles.
# Base case is when level <= 0, which stops further recursion.
# Branch length decreases by dividing by 1.7 each recursive call.

# User Inputs:
# x, y: Starting position of the fractal on the screen.
# levels: Number of recursion levels (integer >=1 recommended)
# colour: Line colour from the available list.

# Test Cases:
# 1) x=0, y=0, levels=2, colour='red'
# Expected: Small triangle fractal at center, 7 recursive calls.
# 2) x=-100, y=-100, levels=3, colour='blue'
# Expected: Larger fractal shifted to bottom-left, 22 recursive calls.

# Reasonable Recursion Depth:
# Too low (1-2): fractal is very simple and not visually interesting.
# Too high (6+): may slow down drawing and clutter the screen.

# Debugging Notes:
# Ensure branch_length > 0 to avoid turtle errors.
# Colour validation prevents invalid colour strings.
# Recursive call counting helps verify recursion works correctly.

# Peer review:
# I tried the code and it works well.
# The triangles draw correctly and colours look good.
# The code is easy to read and the comments help.
# -Daichi
