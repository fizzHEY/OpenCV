import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # 黑色
# print(img)
# img[200:300, 100:300] = 255, 0, 0
# （图片，起点，终点，颜色，厚度）
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)  # 画线
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)  # 画框 cv2.FILLED填充
# 圆心，半径，颜色，厚度
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# 内容，起点，字体，比例，颜色，厚度
cv2.putText(img, "OPEN CV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow("Image", img)

cv2.waitKey(0)
