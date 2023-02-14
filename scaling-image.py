import cv2
import numpy as np

input_image = cv2.imread('numpy-zeros.png')
cv2.imshow('some-image',input_image)
cv2.waitKey()

# making image half of the original size
scaled_image = cv2.resize(input_image,None,fx=0.5,fy=0.5)
cv2.imshow('half-image',scaled_image)
cv2.waitKey()
# making the image 1.5 bigger
upscaled_image = cv2.resize(input_image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_AREA)
cv2.imshow('upscaled_image',upscaled_image)
cv2.waitKey()

skewed_image = cv2.resize(input_image,(700,300),interpolation=cv2.INTER_AREA)
cv2.imshow('skewed_image',skewed_image)
cv2.waitKey()