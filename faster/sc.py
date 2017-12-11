from random import randint

import os
from PIL import Image
path='final'
classnames=os.listdir(path)
images=[]
f1=open('input_index.txt','w')
for temp in classnames:
	
	
	images.append(Image.open('final/'+temp))
	f1.write(temp+"\n")

f1.close()
k=len(images)
im2=[]
for i in range(k):	
	img=images[i]
	im2.append(img)
h=0
for i in range(k):
	h=h+20*im2[i].size[1]/im2[i].size[0]+5

result = Image.new('L', (20,h),'white')
lp=0
for i in range(k):	
	img=im2[i]
	img=img.convert('L')
	print 'before ',
	print img.size
	h=20*img.size[1]/img.size[0]
	if h<1:
		h=1
	img=img.resize((20,h),Image.ANTIALIAS)
	print 'after ',
	print img.size
	result.paste(img, box=(0, lp))
	lp=lp+5+img.size[1]
		
	
result.save('res.png')	
