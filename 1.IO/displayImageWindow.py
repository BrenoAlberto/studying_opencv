import cv2
import numpy as np

img = cv2.imread('RandomColor.png')
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()