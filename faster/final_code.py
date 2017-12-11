import numpy as np
import cv2
import threading
import cv2.cv as cv
from CNN import CNN
from DataSet import *
import os
import sys
import subprocess
import threading
import datetime
import RPi.GPIO as gpio
import time
cwd = os.getcwd()


image_size=30

prev=None



class sound_play(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        #subprocess.call(['omxplayer',self.sound_file])
        gpio.setmode(gpio.BOARD)
        gpio.setup(18,gpio.OUT)
        gpio.output(18,True)
        time.sleep(.5)
        gpio.cleanup()



class Tens:
    
    def __init__(self):
        f1=open('data_set_config.txt','r')
        st=f1.readline()
        st1=st.split(' ')
        global image_size
        image_size=int(st1[0])
        shape=[int(st1[0]),int(st1[1]),int(st1[2])]
        print 'dataset image shape:',st

        class_cnt=int(f1.readline())

        self.class_name=[]

        for i in range(0,class_cnt):
            self.class_name.append(f1.readline().replace('\n',''))
        f1.close()



        print 'initializing CNN...'

        self.cnn=CNN(shape,class_cnt)

        print 'CNN initialized !'
        print 'loading model...'
        self.cnn.load('model')
        print 'model loaded'
        
        
    def detect(self,src):
        global prev
        sr=[]
        #src = cv2.resize(src,(20,20), interpolation = cv2.INTER_CUBIC)
        src=src.reshape([-1])
        #print src.shape
        sr.append(src)
        pred=self.cnn.predict(sr)
        print 'found ',self.class_name[pred[0]]
        
        
        
        current='sound/'+self.class_name[pred[0]]+'.mp3'
        t1=sound_play()
        t1.start()
        if prev !=current:
            
            #subprocess.call(['omxplayer',current])
            prev=current
        return current
            
            

        
        #return self.class_name[pred[0]]


tens=Tens()
        
cap = cv2.VideoCapture(0)

    

try:
    it=0
    while(True):
        print 'f'
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        start_time=datetime.datetime.now()
        #img = cv2.medianBlur(gray,3)
        img = cv2.GaussianBlur(gray,(7,7),0)
        
       

        circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                                param1=50,param2=30,minRadius=30,maxRadius=50)
        if circles is not None:
            print 'yes circle found'
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                if i[0] < i [2] or i[1] < i[2]:
                    continue
                #cv2.imwrite('test/full/'+str(it)+'.jpg',frame)
               
                x1=i[0]-i[2]
                x2=i[0]+i[2]
                y1=i[1]-i[2]
                y2=i[1]+i[2]
                #cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),3)
                cir=gray[y1:y2,x1:x2]
                cir_color=frame[y1:y2,x1:x2]
                #cv2.imwrite('test/detect/'+str(it)+'.jpg',cir)
                
                
                #cv2.imwrite('test/1.jpg',cir)
                
                cir = cv2.resize(cir,(image_size,image_size), interpolation = cv2.INTER_CUBIC)
                cir_color = cv2.resize(cir_color,(image_size,image_size), interpolation = cv2.INTER_CUBIC)

                #cv2.imwrite('test/2.jpg',cir)
                ret3, th3 = cv2.threshold(cir, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
                cir=th3
                
                
                
                
                #cv2.imwrite('test/detect/'+str(it)+'.binary.jpg',th3)
                
                binary_cnt=np.count_nonzero(cir)
                #cir = cv2.medianBlur(cir,7)
                red_cnt=0
                for i in range(0,image_size):
                    for j in range(0,image_size):
                        b=cir_color.item(i,j,0)
                        g = cir_color.item(i, j, 1)
                        r = cir_color.item(i, j, 2)

                        if r>70 and g<70 and b<70:
                            cir_color.itemset((i,j,0),0)
                            cir_color.itemset((i,j,1),0)
                            cir_color.itemset((i,j,2),255)
                            red_cnt+=1
                        else:
                            cir_color.itemset((i, j, 0), 0)
                            cir_color.itemset((i, j, 1), 0)
                            cir_color.itemset((i, j, 2), 0)
                #print 'center,radius=',i,'binary cnt=',binary_cnt,'red cnt=',red_cnt
                #f=open('test/log/'+str(it)+'.txt','w')
                flag= binary_cnt>200 and binary_cnt<400 and red_cnt>6
                #print flag
                s="True" if flag else "False"
                #f.write('binary cnt='+str(binary_cnt)+' red cnt='+str(red_cnt)+'->'+s)
                #f.close()
                #cv2.imwrite('test/detect/'+str(it)+'.red.jpg',cir_color)
                it=it+1
                
                if not flag :
                    continue

                   
                r=tens.detect(cir)
                #subprocess.call(['touch',str(it)+r+'.txt'])
                #a=raw_input()    
                end_time=datetime.datetime.now()
                time_diff=end_time-start_time
                print time_diff
       
        if it>200:
            print 'end'
            cap.release()
            cv2.destroyAllWindows()
            exit()
            
    ##            subprocess.call(['omxplayer',self.sound_file])
except:
    print 'error', sys.exc_info()[0]
    cap.release()
    cv2.destroyAllWindows()
    exit()
    
    
        
    
    
    
    