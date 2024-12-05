import cv2 
import numpy as np  

cap = cv2.VideoCapture("/Volumes/Media/Total-e_2410301250_0001.mov")
prev_frame = np.zeros((2160, 3840, 3))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_no = 0
print("Video FPS: " + str(fps))

while(cap.isOpened()):        
    frame_exists, frame = cap.read()
    if frame_exists:
        diff_index = np.sum(np.abs(frame - prev_frame))
        prev_frame = frame
        if abs(diff_index) > 2:
            print("Glitch detected in static video!")
            print("Frame : " + str(frame_no) + " - Timestamp: ", str(cap.get(cv2.CAP_PROP_POS_MSEC)))
            print(diff_index)
    else:
        print("Stopped!")
        break
    frame_no += 1
    if frame_no % (60 * fps) == 0:
        print(str(frame_no / (60 * fps)) + " min checked.")

cap.release() 