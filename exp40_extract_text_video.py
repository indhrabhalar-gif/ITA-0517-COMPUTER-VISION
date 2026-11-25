# Experiment 40: Extract Text from Videos using OpenCV
import cv2
import numpy as np

def extract_text_regions_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        output = frame.copy()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 100 and h > 15: # Text line filtering
                cv2.rectangle(output, (x-5, y-5), (x+w+10, y+h+10), (0, 0, 255), 2)
                cv2.putText(output, "Extracted Text Region", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
        if frame_idx == 20:
            cv2.imshow("Detected Text in Video", output)
            break
        frame_idx += 1
        
    cap.release()
    cv2.destroyAllWindows()

extract_text_regions_from_video("assets/sample_video.mp4")
