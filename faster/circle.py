import cv2
import cv2.cv as cv
import numpy as np
import sys





img = cv2.imread('full_image/'+sys.argv[1]+'.jpg',0)
cv2.imshow('main image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    
    
    
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=30,maxRadius=50)
if circles is not None:
    print 'yes circle found'
    circles = np.uint16(np.around(circles))

        
    for i in circles[0,:]:
        # draw the outer circle
        x1=i[0]-i[2]
        x2=i[0]+i[2]
        y1=i[1]-i[2]
        y2=i[1]+i[2]
        cir=img[y1:y2,x1:x2]
        #blur = cv2.GaussianBlur(cir, (3, 3), 0)
        ret3, th3 = cv2.threshold(cir, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cir=th3
        cv2.imwrite('dataset/'+sys.argv[1]+'.jpg',cir)
        cv2.imshow('detected circles',cir)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
    
    
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
else:
    print 'no circle found'

#cv2.imshow('detected circles',cimg)
#cv2.waitKey(0)
cv2.destroyAllWindows()