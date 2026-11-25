# Experiment 36: Subtract Background based on color levels using OpenCV
import cv2
import numpy as np

def subtract_background(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_bound = np.array([30, 50, 50])
    upper_bound = np.array([85, 255, 255])
    bg_mask = cv2.inRange(hsv, lower_bound, upper_bound)
    fg_mask = cv2.bitwise_not(bg_mask)
    foreground = cv2.bitwise_and(image, image, mask=fg_mask)
    return image, bg_mask, foreground

image, mask, fg = subtract_background("assets/fruits.jpg")
cv2.imshow("Background Subtracted (Foreground only)", fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
