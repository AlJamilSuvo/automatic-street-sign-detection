import numpy as np
import cv2
import cv2.cv as cv
from CNN import CNN
from DataSet import *
import os
cwd = os.getcwd()

class tens:
    
    def __init__(self):
        f1=open('data_set_config.txt','r')
        st=f1.readline()
        st1=st.split(' ')
        shape=[int(st1[0]),int(st1[1]),int(st1[2])]
        print 'dataset image shape:',st

        class_cnt=int(f1.readline())

        class_name=[]

        for i in range(0,class_cnt):
            class_name.append(f1.readline())
        f1.close()



        print 'initializing CNN...'

        self.cnn=CNN(shape,class_cnt)

        print 'CNN initialized !'
        print 'loading model...'
        self.cnn.load('model')
        print 'model loaded'
        
        







cap = cv2.VideoCapture(0)

    


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img = cv2.medianBlur(gray,3)
    img = cv2.GaussianBlur(gray,(5,5),0)

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
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
    
        
    
    
    
    