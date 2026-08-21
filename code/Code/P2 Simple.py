import cv2

image = cv2.imread('sample_faded.jpg')


blur = cv2.GaussianBlur(image, (5,5), 0)

cv2.imwrite('output.jpg', blur)

cv2.imshow('Original Color Image', image)
cv2.imshow('Processed Color Image', blur)

cv2.waitKey(0)

cv2.destroyAllWindows()
