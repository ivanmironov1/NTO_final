import cv2
import numpy as np
from PIL import Image

img = cv2.imread('data/img_1.png')
print(img)

kernel = np.array([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
])

img1 = cv2.filter2D(img, -1, kernel)

cv2.imshow('src', img)
cv2.imshow('with filter', img1)
cv2.waitKey(0)


