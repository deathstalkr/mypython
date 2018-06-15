from sklearn.datasets  import load_iris
from  sklearn  import  tree
import numpy

a=dir(load_iris())
print(a)
#  loading  iris
iris=load_iris()

x=[50,99,145]
#training
train_target=numpy.delete(iris.target,x)
train_data=numpy.delete(iris.data,x,axis=0)
#test
test_data=iris.data[x]
test_target=iris.target[x]
#  calling  decisiontree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
#  predicting output
predicted=trained.predict(test_data)

#print(predicted)
print("predicted::::",predicted)
print("actual::::",test_target)


#print(predicted)
#  now calculating  accuracy
#from  sklearn.metrics  import  accuracy_score

from  sklearn.metrics  import  accuracy_score

pct=accuracy_score(test_target,predicted)
print(pct)

