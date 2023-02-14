import cv2
import numpy as np

#imread method to read an image
image = cv2.imread("Messi1.webp")
#gives us  the size of our image ,width , height ,channel
# e.g  (1365,2048,3)  if channel was 1 then image would've been
# grayscale
print(image.shape)

#shows the image  - imshow
cv2.imshow('First image',image)
# so the window won't automatically close until we press a key
cv2.waitKey(0)
cv2.imwrite('image1.png',image)
# closes all the windows when we press a key
cv2.destroyAllWindows()
 

# showing our image as a grayscale one 
image2 = cv2.imread('Messi1.webp',0)
cv2.imshow('Second image',image2)
# 0 means how much it will take to close 
# it's the time in miliseconds  , like 6000 would be 6s
cv2.waitKey(0);
# saves the image
cv2.imwrite('image2.png',image2)
cv2.destroyAllWindows()

# showing our image as a grayscale one 
image3 = cv2.imread('Messi1.webp')
grayscaleImage3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)
cv2.imshow('Third image',grayscaleImage3)
# 0 means how much it will take to close 
# it's the time in miliseconds  , like 6000 would be 6s
cv2.waitKey(0);
cv2.imwrite('image3.png',grayscaleImage3)
cv2.destroyAllWindows()

 