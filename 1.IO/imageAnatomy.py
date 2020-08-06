import numpy
import cv2
imgGrayScale = numpy.zeros((3, 3), dtype=numpy.uint8)

print(imgGrayScale)

imgBGR = cv2.cvtColor(imgGrayScale, cv2.COLOR_GRAY2BGR)

print(imgBGR)

print(imgGrayScale.shape)
print(imgBGR.shape)