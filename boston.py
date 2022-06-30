from sklearn.datasets import load_boston
from sklearn.neighbors import  KNeighborsClassifier
#from sklearn.model_selection  import train_test_split
import matplotlib.pyplot  as  py
from  sklearn  import  tree
import numpy as ny
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import random
from sklearn import preprocessing

boston=load_boston()

#assiging random num to x
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res

x=Rand(start=0,end=505,num=5)
print(x)
'''
print(boston.data.shape)
print(dir(boston))
print(boston.data)  
print(boston.target)
print(boston.feature_names)
'''
x_train=ny.delete(boston.data,x,axis=0)
y_train=ny.delete(boston.target,x)

lab_enc = preprocessing.LabelEncoder()
encoded = lab_enc.fit_transform(y_train)

x_test=boston.data[x]
y_test=boston.target[x].round()

#train_test_split(boston.data,boston.target,stratify=boston.target,random_state=42,test_size=0.1)

#training data using Decisiontree

dsc=tree.DecisionTreeClassifier()
trained=dsc.fit(x_train,encoded)

#training data using knn
knn =KNeighborsClassifier(n_neighbors=1)
trainedknn=knn.fit(x_train,encoded)

#training data using SVC
svc=SVC()
trainedsvc=svc.fit(x_train,encoded)

#testing with Decisiontree
output1=trained.predict(x_test)
print('actual: ',y_test)
print(output1)

#accuracy with Decisiontree
acc1=accuracy_score(output1,y_test.round())
print(acc1)

#testing with knn
output=trainedknn.predict(x_test)
print(output)

#accuracy with Knn
acc=accuracy_score(output,y_test.round())
print(acc)

#testing with SVC
output2=trainedsvc.predict(x_test)
print(output2)

#accuracy with SVC
acc2=accuracy_score(output2,y_test.round())
print(acc2)
