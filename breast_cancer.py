from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.model_selection  import train_test_split
import matplotlib.pyplot  as  py
from  sklearn  import  tree
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

cancer=load_breast_cancer()

print(dir(cancer))
print(cancer)
print(cancer.target_names)
print(cancer.feature_names)

#splitting data
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.01)

#training data using Decisiontree
dsc=tree.DecisionTreeClassifier()
traineddsc=dsc.fit(x_train,y_train)

#training data using knn
knn =KNeighborsClassifier(n_neighbors=3)
trainedknn=knn.fit(x_train,y_train)

#training data using SVC
svc=SVC()
trainedsvc=svc.fit(x_train,y_train)

#testing with Decisiontree
output1=traineddsc.predict(x_test)
print(output1)

#accuracy with Decisiontree
acc1=accuracy_score(output1,y_test)
print(acc1)

#testing with knn
output=trainedknn.predict(x_test)
print(output)

#accuracy with Knn
acc=accuracy_score(output,y_test)
print(acc)

#testing with SVC
output2=trainedsvc.predict(x_test)
print(output2)

#accuracy with SVC
acc2=accuracy_score(output2,y_test)
print(acc2)

#plotting graph
py.xlabel('Algorithms')
py.ylabel('Percentage')
algo=['DsT','KNN','SVC']
accuracy_percent=[acc1,acc,acc2]
py.scatter(algo,accuracy_percent,color='r',s=100,marker='x')
py.show()
