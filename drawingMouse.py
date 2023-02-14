import numpy as np
import cv2 

# par means optional parameter , flagval for some warning
def circle_shape(event,x,y,flagval,par):
    # if left button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        #circle receives current window,(x,y) mouse coordinates
        # circle outline color, -1 means circle is filled
        cv2.circle(image_window,(x,y),50,(255,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image_window,(x,y),50,(0,255,255),-1)

# we use it to reference our window  by name
cv2.namedWindow(winname='Image_Window')
# here we specify that we want to trigger the click event on Image_Window
cv2.setMouseCallback('Image_Window',circle_shape)



#black image  !=  Image_Window , we use it for the background
# we used 'Image_Window' for the click event
image_window = np.zeros((1024,1024,3),np.uint8)

while True: 
    cv2.imshow('Image_Window',image_window)
    # waitKey() - returns the value -1 if no key was pressed
    # and the ASCII value of the pressed key,if any
    # 0xFF == 27  means the escape key was pressed
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.destroyAllWindows()
        break 
         
