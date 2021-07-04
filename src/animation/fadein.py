##############################
#
#   Simple OpenCV animation
#
#             by
#
#      Code Monkey King
#
##############################

# packages
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import numpy as np
import random

# open image file
image = cv2.imread('image1.jpg', cv2.IMREAD_UNCHANGED)

# extract width and height from the original image
width = image.shape[1]
height = image.shape[0]

# define video codec
fourcc = VideoWriter_fourcc(*'MP42')

# define video stream
video = VideoWriter('video.avi', fourcc, float(24), (width, height))

# init empty frame
frame = np.zeros((height, width, 3), np.uint8)

# frame count
frame_count = 0

# init random row indexes
random_rows = list(range(len(image)))

# shuffle rows' indexes in random order
random.shuffle(random_rows)

# loop over pixel rows in the original image
for y in random_rows:
    # loop over pixels within a given row
    for x in range(len(image[y])):
        # draw pixel on frame
        cv2.circle(
            frame,                     # frame to write pixel to
            (x, y),                    # center coordinates of a circle
            1,                         # circle radius
            (int(image[y][x][0]),      # pixel RED value
             int(image[y][x][1]),      # pixel GREEN value
             int(image[y][x][2])       # pixel BLUE value
            ), 
            -1                         # thickness
        )
    
    # write video frame
    if (y % 10 == 0):
        frame_count += 1
        video.write(frame)
        print('Writing frame:', frame_count)

# keep image frame for some time...
for i in range(100):
    # write complete frame
    video.write(frame)
    frame_count += 1
    print('Writing frame:', frame_count)

# release video
video.release()

# show image in a window
#cv2.imshow('Image', frame)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

















