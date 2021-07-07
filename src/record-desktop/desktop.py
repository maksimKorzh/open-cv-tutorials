#################################
#
#    Simple desktop recorder
#
#              by
#
#       Code Monkey King
#
#################################

# packages
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import pyautogui as pg
import numpy as np

# create an output video stream
video = VideoWriter('desktop.avi', VideoWriter_fourcc(*'MP42'), 7, (1366, 768))

# main loop
while True:
    # take a screenshot
    screenshot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)

    # write video frame
    video.write(screenshot)

    # display screenshot in a window
    #cv2.imshow('Screenshot', screenshot)

    # escape condition
    if cv2.waitKey(1) & 0xFF == 27: break

# clean ups
cv2.destroyAllWindows()

# release the video stream
video.release()



