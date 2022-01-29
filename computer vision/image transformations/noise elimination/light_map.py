import cv2
import numpy as np
from PIL import Image
import math

img = cv2.imread('data/img_2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img1 = cv2.GaussianBlur(img1, (101, 101), 7)
img2 = img / img1

normalized_image = cv2.normalize(img2, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('src', img)
cv2.imshow('blured', img1)
cv2.imshow('blured_without', img2)
cv2.imshow('normalized_image', normalized_image)
cv2.waitKey(0)