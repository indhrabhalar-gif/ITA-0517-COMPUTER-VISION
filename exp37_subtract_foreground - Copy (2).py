# Experiment 37: Subtract Foreground based on color levels using OpenCV
import cv2
import numpy as np

def subtract_foreground(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    
    fg_mask = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
    bg_preserved_mask = cv2.bitwise_not(fg_mask)
    background_only = cv2.bitwise_and(image, image, mask=bg_preserved_mask)
    return image, fg_mask, background_only

image, mask, bg = subtract_foreground("assets/fruits.jpg")
cv2.imshow("Foreground Subtracted (Background only)", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
