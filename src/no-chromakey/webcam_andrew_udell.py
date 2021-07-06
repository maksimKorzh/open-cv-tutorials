######################################
#
#   Background removal with python
#
#                by
#
#           Andrew Udell
#    (slightly modified by CMK)
#
######################################

# packages
import numpy as np
import cv2
import copy

# Parameters
blur = 21
canny_low = 15
canny_high = 150
dilate_iter = 10
erode_iter = 10
mask_color = (0.0,0.0,0.0)

# initialize video from the webcam
video = cv2.VideoCapture(0)
image = cv2.imread('stars.png')

while True:
    # read frame from webcam
    ret, frame = video.read()
    
    if ret == True:        
        # Convert image to grayscale        
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Canny Edge Dection
        edges = cv2.Canny(image_gray, canny_low, canny_high)
        
        # improve edges
        edges = cv2.dilate(edges, None)
        edges = cv2.erode(edges, None)
        
        # get the contours and their areas
        contour_info = []        
        contours, hierarch = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for con in contours: contour_info.append((con, cv2.contourArea(con)))
        
        # Set up mask with a matrix of 0's
        mask = np.zeros(frame.shape, dtype = np.uint8)
        
        # Go through and find relevant contours and apply to mask
        for contour in contour_info:
            # Instead of worrying about all the smaller contours, if the area is smaller than the min, the loop will break
            mask = cv2.fillConvexPoly(mask, contour[0], (255, 255, 255))

        # use dilate, erode, and blur to smooth out the mask
        mask = cv2.dilate(mask, None, iterations=dilate_iter)
        mask = cv2.erode(mask, None, iterations=erode_iter)
        mask = cv2.GaussianBlur(mask, (blur, blur), 0)
        
        # inversed colors mask
        inverse = np.zeros(frame.shape, dtype = np.uint8)
        inverse.fill(255)
        
        # inverse mask
        inverse = cv2.bitwise_xor(mask, inverse)
        
        # mask background image
        inverse = cv2.bitwise_and(inverse, image)
        
        # blend webcam view and foreground image
        mask = cv2.bitwise_and(mask, frame)
        
        # bundle all together
        mask = cv2.bitwise_or(mask, inverse)
        
        # show frame
        cv2.imshow("Foreground", cv2.bitwise_or(mask, inverse))
        
        # Use the 'Esc' button to quit
        if cv2.waitKey(60) & 0xff == 27: break
    
    else:
        break

# clean ups
cv2.destroyAllWindows()
video.release()
