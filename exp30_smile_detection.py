# Experiment 30: Smile / Mouth Region Detection using OpenCV
import cv2

detector = cv2.FaceDetectorYN_create("assets/face_detection_yunet.onnx", "", (300, 300))
image = cv2.imread("assets/face.jpg")
h, w, _ = image.shape
detector.setInputSize((w, h))

ret, faces = detector.detect(image)
output = image.copy()

if faces is not None:
    for face in faces:
        # Landmarks: Right mouth corner (10, 11), Left mouth corner (12, 13)
        rmx, rmy = int(face[10]), int(face[11])
        lmx, lmy = int(face[12]), int(face[13])
        
        # Smile bounding box around mouth corners
        min_x, max_x = min(rmx, lmx) - 10, max(rmx, lmx) + 10
        min_y, max_y = min(rmy, lmy) - 12, max(rmy, lmy) + 18
        
        cv2.rectangle(output, (min_x, min_y), (max_x, max_y), (0, 0, 255), 2)
        cv2.line(output, (rmx, rmy), (lmx, lmy), (0, 255, 255), 2)
        cv2.putText(output, "Smile Detected", (min_x, min_y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imshow("Smile Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
