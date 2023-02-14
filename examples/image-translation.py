import cv2
import numpy as np

og_image = cv2.imread('numpy-zeros.png')
width,height = og_image.shape[:2]

# this is where we want to move our image by,so we want 
# to add half the width to current image width and half the height
# to current image height
half_width,half_height = width/2,height/2 

# takes in a matrix which has our Tx and Ty (displacements)
translation_matrix = np.float32([[1,0,half_height],[0,1,half_width]])
# takes in original image ,translation matrix and width and height of image
translation = cv2.warpAffine(og_image,translation_matrix,(width,height))
cv2.imshow('translated',translation)
cv2.waitKey(0)
cv2.destroyAllWindows()