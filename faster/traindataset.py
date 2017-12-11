from CNN import CNN
from DataSet import *
import os
cwd = os.getcwd()
print cwd

image_size=30
# A folder will contain multiple folders, each for one class of data.
# For those classes, name will be considered as class name



ds=DataSet.prepare_from_folder(cwd+"/dataset", height=image_size, width=image_size)


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






cnn=CNN(ds.__shape__, ds.__classes__)


file1 = open('data_set_config.txt','w') 
for i in ds.__shape__:
	file1.write(str(i)+" " ) 

file1.write("\n" ) 
file1.write( str(ds.__classes__)+'\n') 
for i in ds.classnames:
	file1.write(i+"\n")

file1.close()
cnn.train(ds, iteration=200,batch_size=64)

cnn.save('model')

cnn.load('model')

#ds.show(ds.images[:20], ds.labels[:20], pred)





#pred=cnn.predict(ds.images[:20])

#pred=cnn.predict(DataSet.readImageToPhoto(20,20,'res.png'))

# Display

#file1 = open('output.txt','w') 


 
 


#for i in pred:

#	file1.write(ds.classnames[i]+'\n') 
	
#file1.close()


