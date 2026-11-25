# Experiment 34: Create white image and draw a Circle using OpenCV
import cv2
import numpy as np

def draw_circle_on_white(width=500, height=400):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    cv2.circle(image, (250, 200), 120, (255, 0, 0), 4)
    return image

img = draw_circle_on_white()
cv2.imshow("Circle on White Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
