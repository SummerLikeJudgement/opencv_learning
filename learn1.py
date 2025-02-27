import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


# 读取图片
## 彩色图片
# img = cv.imread('a.png') # 读取图片
# print(img) # 输出矩阵
# cv.imshow('lty',img) # 输出图片
# cv.waitKey(0) # 按任意键关闭图像或者数字表示等待一定时间消失
# cv.destroyAllWindows()
# print(img.shape) # 返回(h,w,c)/(高度, 宽度, 通道数)

## 显示图像函数
# def cv_show(name, img):
#     cv.imshow(name, img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

## 黑白图片
# img = cv.imread('a.png', cv.IMREAD_GRAYSCALE) # 读取黑白图片
# cv_show('lty', img)
# print(img.shape)
# cv.imwrite('lty.png', img)# 保存图片
# print(type(img))
# print(img.size)
# print(img.dtype)

# 读取视频
vc = cv.VideoCapture("b.mp4")
if vc.isOpened(): # 检查是否正确打开
    open, frame = vc.read()
else:
    open = False

while open:
    ret , frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('result',gray)