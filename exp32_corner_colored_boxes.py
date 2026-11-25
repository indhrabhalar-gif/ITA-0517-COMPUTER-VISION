# Experiment 32: Create white image with 4 colored boxes (Black, Blue, Green, Red) at corners
import cv2
import numpy as np

def create_corner_boxes_image(width=500, height=500):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    box_w = width // 10
    box_h = height // 10
    
    # 1. Top-Left: Black
    image[0:box_h, 0:box_w] = [0, 0, 0]
    # 2. Top-Right: Blue
    image[0:box_h, width-box_w:width] = [255, 0, 0]
    # 3. Bottom-Left: Green
    image[height-box_h:height, 0:box_w] = [0, 255, 0]
    # 4. Bottom-Right: Red
    image[height-box_h:height, width-box_w:width] = [0, 0, 255]
    
    return image

img = create_corner_boxes_image(500, 500)
cv2.imshow("Corner Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
