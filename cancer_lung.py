import pandas as pa
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data=pa.read_excel("cancer patient data sets.xlsx").values
#print(data)
#print(data[0,1:24])
train_data=data[0:998,1:24]
train_target=data[0:998,24]
#print(train_target)
test_data=data[999:,1:24]
test_target=data[999:,24]
print(test_target)
clf=DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
clf1=SVC()
trained1=clf1.fit(train_data,train_target)
clf2=KNeighborsClassifier(n_neighbors=3)
trained2=clf2.fit(train_data,train_target)

predicted=trained.predict([[30,7,7,7,1,7,7,7,7,7,7,7,7,7,7,7,7,1,7,7,7,7,7]])
predicted1=trained1.predict([[30,7,7,7,1,7,7,7,7,7,7,7,7,7,7,7,7,1,7,7,7,7,7]])
predicted2=trained2.predict([[30,7,7,7,1,7,7,7,7,7,7,7,7,7,7,7,7,1,7,7,7,7,7]])

print(predicted)
print(predicted1)
print(predicted2)

#print(test_target)

acc=accuracy_score(predicted,test_target)
print(acc)
acc1=accuracy_score(predicted1,test_target)
print(acc)
acc2=accuracy_score(predicted2,test_target)
print(acc)
#print(train_target)
