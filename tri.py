import numpy as np
import cv2

img = cv2.imread('3.jpg')
img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

new,contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#contours= sorted(contours, key = cv2.contourArea, reverse = True)[:10]

for cnt in contours:
    
     x, y, w, h = cv2.boundingRect(cnt)
     peri = cv2.arcLength(cnt, True)
     approx = cv2.approxPolyDP(c, 0.06 * peri, True)
     print len(approx),w,h
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()