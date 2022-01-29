import cv2
import numpy as np
from PIL import Image

img = cv2.imread('data/img_1.png')

img1 = np.power(img/float(np.max(img)), 1/1.5)
img2 = np.power(img/float(np.max(img)), 1.5)

cv2.imshow('src', img)
cv2.imshow('gamma=1/1.5', img1)
cv2.imshow('gamma=1.5', img2)
cv2.waitKey(0)