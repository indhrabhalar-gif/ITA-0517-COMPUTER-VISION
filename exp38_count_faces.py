# Experiment 38: Count number of faces in an image using OpenCV
import cv2

detector = cv2.FaceDetectorYN_create("assets/face_detection_yunet.onnx", "", (300, 300))
image = cv2.imread("assets/multi_faces.jpg")
h, w, _ = image.shape
detector.setInputSize((w, h))

ret, faces = detector.detect(image)
output = image.copy()

count = len(faces) if faces is not None else 0
if faces is not None:
    for i, face in enumerate(faces, 1):
        x, y, fw, fh = int(face[0]), int(face[1]), int(face[2]), int(face[3])
        cv2.rectangle(output, (x, y), (x + fw, y + fh), (0, 255, 0), 2)
        cv2.putText(output, f"Face #{i}", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.putText(output, f"Total Faces Counted: {count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
print(f"Total number of faces: {count}")

cv2.imshow("Face Counter", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
