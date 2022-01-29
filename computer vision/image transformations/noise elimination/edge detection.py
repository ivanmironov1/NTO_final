import cv2
import numpy as np
from PIL import Image

img = cv2.imread('data/img_1.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

kernel = np.array([
  [-1, -1, -1],
  [-1, 8, -1],
  [-1, -1, -1]
])

kernel1 = np.array([
  [0, -1],
  [1, 0],
])

kernel2_vert = np.array([
  [-1, -1, -1],
  [0, 0, 0],
  [1, 1, 1]
])

kernel2_hor = np.array([
  [-1, 0, 1],
  [-1, 0, 1],
  [-1, 0, 1]
])

kernel3_hor = np.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])

img1 = cv2.filter2D(img_gray, -1, kernel3_hor)

cv2.imshow('src', img)
cv2.imshow('with filter', img1)

cv2.waitKey(0)