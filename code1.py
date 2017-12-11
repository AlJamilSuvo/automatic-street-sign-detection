import RPi.GPIO as gpio
import time

from Tkinter import *

root = Tk()

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)

def forward(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
    
def left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

def key(event):
    print "pressed", repr(event.char)
    sleep_time=.020
    if event.char=='w':
	print 'going forward'
    	forward(sleep_time)
    elif event.char=='s':
	print 'going reverse'
	reverse(sleep_time)
    elif event.char=='a':
        print 'going left'
        left(sleep_time)
    elif event.char=='d':
        print 'going right'
        right(sleep_time)



def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y


frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
root.mainloop()

