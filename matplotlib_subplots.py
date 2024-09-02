# 이미지 4장
import cv2,sys
from matplotlib import pyplot as plt

# 이미지4장 가져오기
imgBGR1 = cv2.imread("cat.jpg")
imgBGR2 = cv2.imread("cat1.jpg")
imgBGR3 = cv2.imread("cat2.jpg")
imgBGR4 = cv2.imread("cat3.jpg")

if imgBGR1 is None or imgBGR2 is None \
    or imgBGR3 is None or imgBGR4 is None:
    sys.exit("image load is failed")
    
    
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

#matplotlib의 plt.subplots로 이미지를 출력
figsize = (10,10)
fig,ax = plt.subplots(2,2, figsize=figsize)

ax[0][0].axis("off")
ax[0][1].axis("off")
ax[1][0].axis("off")
ax[1][1].axis("off")


ax[0][0].imshow(imgRGB1, aspect="auto")
ax[0][1].imshow(imgRGB2, aspect="auto")
ax[1][0].imshow(imgRGB3, aspect="auto")
ax[1][1].imshow(imgRGB4, aspect ="auto")


fig.canvas.manager.set_window_title("sample windows")
plt.show()
