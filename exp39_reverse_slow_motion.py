# Experiment 39: Play video in Reverse Mode in Slow Motion
import cv2

cap = cv2.VideoCapture("assets/sample_video.mp4")
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'): # Slow motion delay = 100ms
        break

cv2.destroyAllWindows()
