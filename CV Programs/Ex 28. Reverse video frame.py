import cv2
input_video_path = "C:/Users/GOKUL/Downloads/video (2160p).mp4"
cap = cv2.VideoCapture(input_video_path)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))
total_frames = int(cap.get(7))
output_video_path = 'reversed_C:/Users/GOKUL/Downloads/video (2160p).mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
for frame_number in range(total_frames - 1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    
    if not ret:
        break
    
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
