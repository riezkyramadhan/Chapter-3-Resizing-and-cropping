import cv2

img = cv2.imread("img.jpg")
print(img.shape)

img_resize = cv2.resize(img, (640,480))
print(img_resize.shape)

img_cropping = img_resize[0:120,480:640] #y=0-120, x=480-640
print(img_cropping.shape)

cv2.imshow("img", img)
cv2.imshow("Resize", img_resize)
cv2.imshow("cropping", img_cropping)
cv2.waitKey(0)