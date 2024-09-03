import numpy as np
import cv2
img = np.full((400,400,3),255,np.uint8)


#line
pt1 = (50,100)
pt2 = (img.shape[0]-50,100)
pt3 = (img.shape[0]-50,300)
lineColor = (0,0,255)
thick=3
lineType = cv2.LINE_8
cv2.line(img,pt1,pt2, lineColor,thick,lineType)
cv2.line(img,pt1,pt3, lineColor,thick,cv2.LINE_AA)


# text = "Hello OpenCV!"
# font = cv2.FONT_HERSHEY_SIMPLEX
# fontSize=1
# BlueColor = (255,0,0)
# thick = 1
# lineType = cv2.LINE_AA
# cv2.putText(img,text,(50,350),font,fontSize,BlueColor,thick,lineType)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()