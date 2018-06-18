from sklearn.tree import DecisionTreeClassifier
#import numpy as ny
#import matplotlib.pyplot as py------for plotting graph
import pandas as pd

data= pd.read_csv("/home/inferni/Downloads/train.csv").values
#print(data)
train_data=data[0:40000,1:]
train_target=data[0:40000,0]

test_data=data[40000:,1:]
test_target=data[40000:,0]

clf=DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
#----f=open('accuracy.txt','w')-------uncomment the below commented line to save the output in a file
predicted=trained.predict(test_data)
print(predicted) #-----print(predicted, file=f)
#print(test_target, file=f)

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(predicted,test_target)

print(accuracy)#------print(accuracy, file=f)
