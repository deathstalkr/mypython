from sklearn.tree import DecisionTreeClassifier
#import numpy as ny
#import matplotlib.pyplot as py------for plotting graph
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

data= pd.read_csv("/home/inferni/Downloads/train.csv").values
#print(data)
#x=dir(data)
#print(x)

#splitting data
train_data=data[0:40000,1:]
train_target=data[0:40000,0]

test_data=data[40000:,1:]
test_target=data[40000:,0]

#training data with decision tree
clf=DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)

#trainig with SVC
clfsvc=SVC()
trainedsvc=clfsvc.fit(train_data,train_target)

#training with KNN
clfknn=KNeighborsClassifier(n_neighbors=3)
trainedknn=clfknn.fit(train_data,train_target)

              #----f=open('accuracy.txt','w')-------uncomment the below commented line to save the output in a file

#testing data with decision tree
predicted=trained.predict(test_data)
print(predicted)                                #-----print(predicted, file=f)
                                                #print(test_target, file=f)
 #accuracy test for decision tree
acc=accuracy_score(predicted,test_target)
print(acc)                                 #------print(accuracy, file=f)

#testing data with svc
predictedsvc=trainedsvc.predict(test_data)
print(predictedsvc)

#accuracy test for SVC
acc1=accuracy_score(predictedsvc,test_target)
print(acc1)

#testing data with KNN
predictedknn=trainedknn.predict(test_data)
print(predictedknn)

#accuracy test for KNN
acc2=accuracy_score(predictedknn,test_target)
print(acc2)
