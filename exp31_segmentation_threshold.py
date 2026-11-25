# Experiment 31: Image Segmentation based on threshold values
import cv2

image = cv2.imread("assets/scene.jpg", cv2.IMREAD_GRAYSCALE)

_, bin_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adapt_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Binary Threshold (127)", bin_thresh)
cv2.imshow("Otsu Threshold", otsu_thresh)
cv2.imshow("Adaptive Threshold", adapt_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
