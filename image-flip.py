import cv2


img = cv2.imread('numpy-zeros.png')

# 0 means vertical flip , 1 horizontal
flipped_vertically_img = cv2.flip(img,0)
flipped_horizontally_img = cv2.flip(img,1)

cv2.imshow('vertical_flip',flipped_vertically_img)
cv2.imshow('horizontal_flip',flipped_horizontally_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

