from sklearn.datasets  import load_digits
from  sklearn  import  tree
import numpy as ny
import matplotlib.pyplot as py
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

digits=load_digits()

#splitting data

train_data=ny.delete(digits.data,-1,axis=0)
train_target=ny.delete(digits.target,-1)
test_target=(digits.target[-10].reshape(1,))  #print(test_target.shape)

#training data using support vector
clf=SVC()
trained=clf.fit(train_data,train_target)

#training data using decision tree
clf1=tree.DecisionTreeClassifier()
trained1=clf1.fit(train_data,train_target)

#training using knn
clf2=KNeighborsClassifier(n_neighbors=3)
trained2=clf2.fit(train_data,train_target)

#testing for SVC
output=trained.predict(digits.data[-10].reshape(1,64))
print(output)

#accuracy test for SVC
acc=accuracy_score(output,test_target)
print(acc)

#testing decision tree data
output1=trained1.predict(digits.data[-10].reshape(1,64))
print(output1)

#accuracy test for decision tree
acc1=accuracy_score(output1,test_target)
print(acc1)

#testing knn
output2=trained2.predict(digits.data[-10].reshape(1,64))
print(output2)

#accuracy test for knn
acc2=accuracy_score(output2,test_target)
print(acc2)

#actual output in image
py.imshow(digits.images[-10])
py.show()

#plotting graph
py.xlabel('Algorithms')
py.ylabel('Percentage')
algo=['DsT','KNN','SVC']
accuracy_percent=[acc1,acc2,acc]
py.scatter(algo,accuracy_percent,color='r',s=100,marker='x')
py.show()
