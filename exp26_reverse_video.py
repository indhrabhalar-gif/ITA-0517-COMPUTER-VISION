# Experiment 26: Reverse the frames of video using OpenCV
import cv2

cap = cv2.VideoCapture("assets/sample_video.mp4")
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("results/reversed_video.mp4", fourcc, 20.0, (frames[0].shape[1], frames[0].shape[0]))
for frame in reversed(frames):
    out.write(frame)
out.release()
print("Reversed video created successfully.")
