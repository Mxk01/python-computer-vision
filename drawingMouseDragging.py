import cv2
import numpy as np


# check if the mouse is currently dragged
isDrawing = False
mouseX,mouseY = -1,1

# creating the window image
image_window = np.zeros((1024,1024,3),np.uint8)
# we use it to reference our window  by name
cv2.namedWindow(winname='Image_Window')



def draw_rectangle(event,x,y,flagval,par):
    global isDrawing,mouseX,mouseY 
    if(event == cv2.EVENT_LBUTTONDOWN):
          isDrawing = True 
          # storing the current x and y coordinates of mouse
          mouseX,mouseY = x,y 
    if(event == cv2.EVENT_MOUSEMOVE):
          # if user is moving mouse  and is drawing 
          if(isDrawing == True):
              # drawing a rectangle from old mouse position to current mouse position , with color (255,255,0) 
              # filled
              cv2.rectangle(image_window,(mouseX,mouseY),(x,y),(255,255,0),-1) 
    if(event==cv2.EVENT_LBUTTONUP):
            # means we stopped drawing 
            isDrawing = False          
            cv2.rectangle(image_window,(mouseX,mouseY),(x,y),(255,255,0),-1) 



# adding event to window named Image_Window
cv2.setMouseCallback('Image_Window',draw_rectangle)

while True: 
    # showing the black bakground image_window on our window
    cv2.imshow('Image_Window',image_window)
    # waitKey() - returns the value -1 if no key was pressed
    # and the ASCII value of the pressed key,if any
    # 0xFF == 27  means the escape key was pressed
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.destroyAllWindows()
        break 
         