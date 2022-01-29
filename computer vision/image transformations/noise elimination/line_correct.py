import cv2
import numpy as np
from PIL import Image

img = cv2.imread('data/img_1.png')

resize_coef = 1
img = cv2.resize(img, None, fx=resize_coef, fy=resize_coef)

cv2.imshow('opencvImage', img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imshow('opencvImage', img)
cv2.waitKey(0)

max_saturation = 0
min_saturation = 255
for i in img[:, :, 1]:
    max_saturation = max(max_saturation, max(i))
    min_saturation = min(min_saturation, min(i))

print(max_saturation, min_saturation)
delta = max_saturation - min_saturation


correct_img = [[[0, 0, 0] for j in range(len(img[0]))] for i in range(len(img))]
for i in range(len(img)):
    for j in range(len(img[0])):
        saturation = img[i][j][1]
        correct_saturation = int((saturation - min_saturation) * (256 / delta))

        correct_img[i][j] = [img[i][j][0], correct_saturation, img[i][j][1]]

correct_img = np.array(correct_img)
correct_img = cv2.cvtColor(np.array(correct_img.astype(np.uint8)), cv2.COLOR_HSV2RGB)

cv2.imshow('opencvImage', correct_img)
cv2.waitKey(0)