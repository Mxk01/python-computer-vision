import numpy as np 
import cv2 
import math 



image_window = np.zeros((1024,1024,3),np.uint8)
cv2.namedWindow('Circle_Window')
 
radius = 15 
mouseCircleX,mouseCircleY = -1,1
isDrawing = False
def drawCircle(event,x,y,flagval,par):
     global isDrawing,mouseCircleX,mouseCircleY,radius

     if(event == cv2.EVENT_LBUTTONDOWN):
       isDrawing = True
       mouseCircleX,mouseCircleY = x,y
    
     if(event == cv2.EVENT_MOUSEMOVE):
        isDrawing = True 
    
     if(event == cv2.EVENT_LBUTTONUP):
       # distance formula
       # radical din  x curent - x initial ^ 2   +  y curent - y initial  ^ 2 
       radius = int(math.sqrt(((mouseCircleX-x)**2) + ((mouseCircleY-y)**2)))
       # mouseCircleX =  x curent , mouseCircleY - y curent 
       cv2.circle(image_window,(mouseCircleX,mouseCircleY),radius,(255,200,0),-1)

cv2.setMouseCallback('Circle_Window',drawCircle)
while True: 
    # showing the black bakground image_window on our window
    cv2.imshow('Circle_Window',image_window)
    # waitKey() - returns the value -1 if no key was pressed
    # and the ASCII value of the pressed key,if any
    # 0xFF == 27  means the escape key was pressed
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.destroyAllWindows()
        break 