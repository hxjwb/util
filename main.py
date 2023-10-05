import cv2


file = r"C:\Users\Administrator\Desktop\peer test\av_frame_.yuv"
#h265_av_frame.yuv

file2 = r"C:\Users\Administrator\Desktop\peer test\h265_av_frame.yuv"
# 读取YUV420文件

import os


width, height = 384, 180

# w2,h2 = 960, 540
# 读取YUV420文件
import numpy as np
data = np.fromfile(file, dtype=np.uint8)

data2 = np.fromfile(file2, dtype=np.uint8)
fs = width*height

dataY = data[0:fs].reshape(height,width)

dataY2 = data2[0:fs].reshape(height,width)


# f2 = w2 * h2
# dataU = data[fs:fs+f2].reshape(h2,w2)
# resize to 1/2


cv2.imshow("Y", dataY)
cv2.imshow("Y2", dataY2)
# cv2.imshow("U", dataU)
# save
cv2.imwrite("Y.png", dataY)
cv2.imwrite("Y2.png", dataY2)
# cv2.imwrite("U.png", dataU)
cv2.waitKey(0)
