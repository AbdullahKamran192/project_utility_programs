import cv2
import numpy as np

# Read image
img = cv2.imread("data/plate8.jpg")

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Use morphological operations to estimate background (shadows)
dilated = cv2.dilate(gray, np.ones((15,15), np.uint8))
bg = cv2.medianBlur(dilated, 21)

# Subtract background and normalize
diff = 255 - cv2.absdiff(gray, bg)
norm = cv2.normalize(diff, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Merge with original color
result = cv2.cvtColor(norm, cv2.COLOR_GRAY2BGR)

cv2.imwrite("output.jpg", result)
