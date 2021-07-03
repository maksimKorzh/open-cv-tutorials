#####################################
#
#  Simple python script to extract 
#        edges from images
#
#               by
#
#        Code Monkey King
#
#####################################

# packages
import cv2

# load image file
image = cv2.imread('image.jpeg', cv2.IMREAD_UNCHANGED)

# convert image to greyscale
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# reduce image noice
image_blur = cv2.medianBlur(image_greyscale, 9)

# extract edges
image_edges = cv2.adaptiveThreshold(
    image_blur,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    blockSize=7,
    C=2
)

# convert image to greyscale cartoon style
image_cartoon = cv2.bitwise_and(image_greyscale, image_edges)

# write output images
cv2.imwrite('image_edges.png', image_edges)         # bare edges
cv2.imwrite('image_cartoon.png', image_cartoon)       # cartoon style

# display image in a window
cv2.imshow('Image', image_cartoon)

# break out of a program
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()
