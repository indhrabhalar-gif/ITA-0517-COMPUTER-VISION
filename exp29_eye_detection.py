# Experiment 29: Eye Detection using OpenCV
import cv2

# Using Face Detector landmarks (Right eye: pts 4,5; Left eye: pts 6,7)
detector = cv2.FaceDetectorYN_create("assets/face_detection_yunet.onnx", "", (300, 300))
image = cv2.imread("assets/face.jpg")
h, w, _ = image.shape
detector.setInputSize((w, h))

ret, faces = detector.detect(image)
output = image.copy()

if faces is not None:
    for face in faces:
        # Landmarks: Right Eye (index 4, 5) and Left Eye (index 6, 7)
        rex, rey = int(face[4]), int(face[5])
        lex, ley = int(face[6]), int(face[7])
        
        cv2.circle(output, (rex, rey), 15, (255, 0, 0), 2)
        cv2.putText(output, "Right Eye", (rex - 25, rey - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
        cv2.circle(output, (lex, ley), 15, (255, 0, 0), 2)
        cv2.putText(output, "Left Eye", (lex - 25, ley - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imshow("Eye Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
