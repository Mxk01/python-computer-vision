import cv2 
import numpy as np 


input_image = cv2.imread('numpy-zeros.png')
cv2.imshow('original_image',input_image)

# input_image.shape gives us width and height of an image
# we destructure it and then we can use those variables
width,height = input_image.shape[:2]

# getRotationMatrix receives couple of parameters 
# image center  -> (width/2,height/2)
# rotation angle  degrees (30,45,etc.) 
# scale .5
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),35,.5)
# takes in original image,rotation matrix and width and height of original image
rotated_image = cv2.warpAffine(input_image,rotation_matrix,(width,height))

cv2.imshow('rotated_image',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()