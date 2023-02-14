import cv2 
import numpy as np

# Creates a black image
# Creates an array   (width,height,channel) of type unsigned int
# makes an 1024 by 1024 matrix filled with black pixels 
black_image = np.zeros((1024,1024,3),np.uint8)
cv2.imshow('dark_image',black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

colorful_line = np.zeros((550,550,3),np.uint8)
# (1,1) represent the starting point
# (250,250) represents the ending point
# (130,155,0) represents the color of our line
# last parameter is the thickness of our line
cv2.line(colorful_line,(1,1),(250,250),(100,255,0),4)
cv2.line(colorful_line,(250,250),(500,0),(100,255,0),4)

cv2.imshow('colorful',colorful_line)
cv2.waitKey(0)
cv2.destroyAllWindows();


circle_image = np.zeros((400,400,3),np.uint8)
# (200,200) is the origin 
# 75 is the radius 
# -1 means the circle is filled
# if we want to add line thickness we can change it to 2,3,4 etc
cv2.circle(circle_image,(200,200),75,(255,222,0),-1)
cv2.imshow('circle_image',circle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


rectangle = np.zeros((512,512,3),np.uint8)

cv2.rectangle(rectangle,(50,50),(250,250),(133,133,0),-1)
cv2.imshow('rectangle',rectangle)
cv2.waitKey()
cv2.destroyAllWindows()


background = np.zeros((300,300,3),np.uint8)
# array of point coordinates [25,65] starting coordinate
# [415,65] coordinates
points = np.array([[25,65],[415,65],[80,150],[400,500]],np.int32)
points = points.reshape((-1,1,2))

# [pts] coordinates of our polygon
# (255,255,255) color
# 3 line thickness
# True  means we want the lines of the polygon to be connected
cv2.polylines(background,[points],True,(255,255,255),3)
cv2.imshow("polygon",background)
cv2.waitKey(0)
cv2.destroyAllWindows()


background2 = np.zeros((400,400,3),np.uint8)
points2 = np.array([[15,35],[44,35],[60,100],[65,150]],np.int32)
points2.reshape(-1,1,2)
cv2.polylines(background2,[points2],True,(155,100,33),4)
cv2.imshow("testing polygons",background2)
cv2.waitKey(0)
cv2.destroyAllWindows()

background3 = np.zeros((444,444,3),np.uint8)
points3 = np.array([[40,150],[70,150],[90,333],[120,455]],np.int32)
points3.reshape(-1,1,2)
cv2.polylines(background3,[points3],True,(200,160,0),4)
cv2.imshow("polygon3",background3)
cv2.waitKey(0)
cv2.destroyAllWindows()