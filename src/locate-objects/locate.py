##3##############################
#
#  Script to locate objects on
#        on a screenshot
#
#               by
#
#        Code Monkey King
#
#################################

# packages
import cv2
import numpy as np
import pyautogui as pg

# take a screenshot to store locally
#screenshot = pg.screenshot('screenshot.png')

# take a screenshot to locate objects on
screenshot = pg.screenshot()

# adjust colors
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# locate a single object in a screenshot
#board = pg.locateOnScreen('board.png')

# draw rectangle around the object
#cv2.rectangle(
#    screenshot,
#    (board.left, board.top),
#    (board.left + board.width, board.top + board.height),
#    (0, 255, 255),
#    2
#)

# detect several objects on screenshot
for pawn in pg.locateAllOnScreen('pawn.png', confidence=0.5):
    # draw rectangle around the object
    cv2.rectangle(
        screenshot,
        (pawn.left, pawn.top),
        (pawn.left + pawn.width, pawn.top + pawn.height),
        (0, 0, 255),
        2
    )

# display screenshot in a window
cv2.imshow('Screenshot', screenshot)

# escape condition
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()


