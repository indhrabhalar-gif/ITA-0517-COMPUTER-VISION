# Experiment 33: Create white image and draw a Rectangle using OpenCV
import cv2
import numpy as np

def draw_rectangle_on_white(width=500, height=400):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.rectangle(image, (100, 80), (400, 320), (0, 0, 255), 4)
    return image

img = draw_rectangle_on_white()
cv2.imshow("Rectangle on White Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
