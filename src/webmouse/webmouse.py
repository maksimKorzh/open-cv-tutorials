#####################################
#
#  Script to control mouse pointer
#     using webcam based input
#
#                by
#
#         Code Monkey King
#
#####################################

# packages
import cv2
import pyautogui as pg

# open webcam stream
webcam = cv2.VideoCapture(0)

# define global mouse coords
old_x = int(1366 / 2)
old_y = int(768 / 2)

# main loop
while True:
    # capture frame from webcam
    stream_ok, frame = webcam.read()
    
    # convert frame to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detect edges
    frame_edges = cv2.Canny(frame_grayscale, 200, 300)
    
    # smooth edges
    frame_edges = cv2.dilate(frame_edges, None)
    frame_edges = cv2.erode(frame_edges, None) 
    
    # detect contours
    contours, hierarchy = cv2.findContours(frame_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # draw touchpad, left and right buttons
    cv2.rectangle(frame, (130, 0), (500, 200), (0, 255, 0), 2)    # touchpad
    cv2.rectangle(frame, (100, 0), (130, 200), (255, 0, 0), 2)    # left button
    cv2.rectangle(frame, (500, 0), (530, 200), (0, 0, 255), 2)    # rigth button
    
    # loop over contours
    for index in range(len(contours)):
        # skip contours with small areas
        if cv2.contourArea(contours[index]) > 12.0:
            # get starting point's coords in the contour
            x = contours[index][0][0][0]
            y = contours[index][0][0][1]
            
            # get point only in specific area
            if y < 200:
                # handle mouse movements
                if x > 130 and x < 500:
                    # draw starting point in the frame
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), 5)
                    
                    # move mouse pointer
                    if x > old_x: pg.moveRel(5, 0)
                    if x < old_x: pg.moveRel(-5, 0)
                    if y > old_y: pg.moveRel(0, 5)
                    if y < old_y: pg.moveRel(0, -5)
                    
                    # update global coordinate
                    old_x, old_y = x, y
                
                # handle left button click
                if x > 100 and x < 130:
                    # draw starting point in the frame
                    cv2.circle(frame, (x, y), 5, (255, 0, 0), 5)
                    
                    # left click mouse
                    pg.click()
                
                # handle right button click
                if x > 500 and x < 530:
                    # draw starting point in the frame
                    cv2.circle(frame, (x, y), 5, (0, 0, 255), 5)
                    
                    # right click mouse
                    pg.click(button='right')

    # smooth edges
    frame_edges = cv2.dilate(frame_edges, None)
    frame_edges = cv2.erode(frame_edges, None)
    
    # if webcam is available
    if stream_ok:
        # show next frame in a window
        cv2.imshow('Webmouse', frame)
        
        # escape condition
        if cv2.waitKey(1) & 0xFF == 27: break

# clean ups
cv2.destroyAllWindows()

# close webcam stream
webcam.release()
