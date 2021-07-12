######################################
#
#  Script to crop image using OpenCV
#
#                 by
#
#          Code Monkey King
#
######################################

# Box(left=5, top=141, width=401, height=399)

# packages
import cv2

# open local image file
screenshot = cv2.imread('screenshot.png')

# crop image [y: y + height, x: x + width]
crop_image = screenshot[141:141 + 399, 5: 5 + 401]

# display image
cv2.imshow('Screenshot', crop_image)

# write cropped image to a file
cv2.imwrite('board.png', crop_image)

# escape condition
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()

