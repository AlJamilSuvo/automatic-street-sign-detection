from CNN import CNN
import cv2
import os
cwd = os.getcwd()
print 'start'
#print cwd
# A folder will contain multiple folders, each for one class of data.
# For those classes, name will be considered as class name



#ds=DataSet.prepare_from_folder(cwd+"/dataset_temp", height=20, width=20)


'''
l=ds.make_folds()
i=0
to=0
for il in l:
	cnn=CNN(ds.__shape__, ds.__classes__)
	k=cnn.trainWithFold(il, iteration=200,batch_size=64)
	print 'printed'
	to=to+k
	i=i+1


print "Tenfold:"
print to/i
'''

f1=open('data_set_config.txt','r')
st=f1.readline()
st1=st.split(' ')
shape=[int(st1[0]),int(st1[1]),int(st1[2])]
print st

class_cnt=int(f1.readline())

class_name=[]

for i in range(0,class_cnt):
    class_name.append(f1.readline().replace('\n',''))
f1.close()



print 'before cnn call'

cnn=CNN(shape,class_cnt)

print 'after cnn call'
'''
file1 = open('data_set_config.txt','w') 
for i in ds.__shape__:
	file1.write(str(i)+" " ) 

file1.write("\n" ) 
file1.write( str(ds.__classes__)+'\n') 
for i in ds.classnames:
	file1.write(i+"\n")

file1.close()
cnn.train(ds, iteration=100,batch_size=64)

cnn.save('model')
'''
print 'loading model...'
cnn.load('model')
print 'model loaded'

#ds.show(ds.images[:20], ds.labels[:20], pred)





#pred=cnn.predict(ds.images[:20])
sr=[]
src=cv2.imread('final/res.jpg',0)
src = cv2.resize(src,(20,20), interpolation = cv2.INTER_CUBIC)
src=src.reshape([-1])
print src.shape
sr.append(src)
pred=cnn.predict(sr)


# Display

file1 = open('output.txt','w')


 
 


for i in pred:
    file1.write(class_name[i]+'\n')
    print '--------','Final Result :',class_name[i],'----------'
	
file1.close()

