################################
#
#   Record video from webcam
#
#             by
#
#      Code Monkey King
#
################################

# packages
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

# open the webcam video stream
webcam = cv2.VideoCapture(0)

# open output video file stream
video = VideoWriter('webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))

# main loop
while True:
    # get the frame from the webcam
    stream_ok, frame = webcam.read()
    
    # if webcam stream is ok
    if stream_ok:
        # display current frame
        cv2.imshow('Webcam', frame)
        
        # write frame to the video file
        video.write(frame)

    # escape condition
    if cv2.waitKey(1) & 0xFF == 27: break

# clean ups
cv2.destroyAllWindows()

# release web camera stream
webcam.release()

# release video output file stream
video.release()







    
