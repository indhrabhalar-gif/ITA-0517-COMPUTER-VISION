# Experiment 35: Put Text string on image using OpenCV
import cv2

def put_text_on_image(image_path, text="SIMATS Engineering - Vision Lab"):
    image = cv2.imread(image_path)
    org = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, org, font, 1.0, (0, 255, 255), 2, cv2.LINE_AA)
    return image

img = put_text_on_image("assets/scene.jpg")
cv2.imshow("Text on Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
