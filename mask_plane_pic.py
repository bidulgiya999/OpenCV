import cv2,sys

# 이미지 불러오기(load img)
src = cv2.imread("airplane.bmp")
mask = cv2.imread("mask_plane.bmp",cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("field.bmp")

# 이렇게 영상처리함
# 마스크 연산
cv2.copyTo(src,mask,dst)

cv2.imshow("img",dst)
cv2.waitKey()
cv2.destroyAllWindows()
