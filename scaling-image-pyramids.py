import cv2

# A pyramid is a set of images which are arranged like a pyramid format
image = cv2.imread("numpy-zeros.png")

# scales down 
smaller_img = cv2.pyrDown(image)
# scales up 
larger_img = cv2.pyrUp(smaller_img)


cv2.imshow('original-image',image)
cv2.imshow('larger-image',larger_img)
cv2.imshow('smaller-image',smaller_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
  