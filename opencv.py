import cv2
import sys
fileName = "cat.jpg"

img = cv2.imread(fileName)
print(img.shape)
#예외처리 루틴 : 이미지를 읽어오지 못했을때
if img is None:
    print("image load fail")
    sys.exit()
    
# 창에 이미지를 출력
# 창의 이름을 img
cv2.namedWindow("img", cv2.WINDOW_FREERATIO)
#img창에 img 배열을 출력
cv2.imshow("img",img)
# 키보드 입력을 기다리는 함수
# q키를 눌렀을때 창이 종료되게
loop = True
while(loop):
    if cv2.waitKey() == ord("q"):
# 모든 창  닫기
        cv2.destroyAllWindows()
        loop = False
        
        # 히스토그램 평활화
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_eq = cv2.equalizeHist(img_gray)

        # 평활화된 이미지 출력
        cv2.imshow("Equalized Image", img_eq)

        # 키보드 입력을 기다리는 함수
        # q키를 눌렀을 때 창이 종료되게
        while True:
            if cv2.waitKey() == ord("q"):
                # 모든 창 닫기
                cv2.destroyAllWindows()
                break
    