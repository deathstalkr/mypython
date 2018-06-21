from sklearn.datasets  import load_digits
from  sklearn  import  tree
#import numpy as ny
import matplotlib.pyplot as py
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

digits=load_digits()
print(dir(digits))
#print(digits)
#splitting data

train_data,test_data,train_target,test_target=train_test_split(digits.data,digits.target,test_size=0.0001)

# trainig with decision tree

clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)

#trainig with knn

clfknn=KNeighborsClassifier(n_neighbors=10)
trained1=clfknn.fit(train_data,train_target)

#testing data with decision tree

predicted=trained.predict(test_data)
print(predicted)
print('\n',test_target)

#accuracy test for decision tree

accuracy=accuracy_score(predicted,test_target)
print(accuracy)

#testing with knn

predictedknn=trained1.predict(test_data)
print(predictedknn)

#accuracy test for knn

acc=accuracy_score(predictedknn,test_target)
print(acc)
