import cv2 
import numpy as np

black_image = np.zeros((300,300,3),np.uint8)
# (10,100) text position x,y on screen
# (155,100,0) - represents font color 
# 4 is thickness of text
cv2.putText(black_image,'Some text',(10,100),
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,
            (155,100,0),4,cv2.LINE_AA

            )
cv2.imshow('Testing text',black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()