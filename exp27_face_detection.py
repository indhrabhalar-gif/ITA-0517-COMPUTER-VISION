# Experiment 27: Face Detection using OpenCV
import cv2

# Initialize Face Detector (cv2.FaceDetectorYN / Haar / DNN)
detector = cv2.FaceDetectorYN_create("assets/face_detection_yunet.onnx", "", (300, 300))
image = cv2.imread("assets/face.jpg")
h, w, _ = image.shape
detector.setInputSize((w, h))

ret, faces = detector.detect(image)
output = image.copy()

if faces is not None:
    for face in faces:
        x, y, fw, fh = int(face[0]), int(face[1]), int(face[2]), int(face[3])
        confidence = face[-1]
        cv2.rectangle(output, (x, y), (x + fw, y + fh), (0, 255, 0), 3)
        cv2.putText(output, f"Face: {confidence:.2f}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Detected Faces", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
