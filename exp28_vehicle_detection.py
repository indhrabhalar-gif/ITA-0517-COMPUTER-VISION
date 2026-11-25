# Experiment 28: Vehicle Detection in video frames
import cv2

cap = cv2.VideoCapture("assets/sample_video.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=25)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    _, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 200:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Vehicle Detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            
    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
