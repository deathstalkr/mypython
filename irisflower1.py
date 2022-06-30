from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as py

# loading iris
iris = load_iris()
print(iris)
train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.1)

#  calling  decisiontree
clf = tree.DecisionTreeClassifier()
trained = clf.fit(train_data, train_target)

# calling knn
clfknn = KNeighborsClassifier(n_neighbors=3)
trained1 = clfknn.fit(train_data, train_target)

# calling SVC
clfsvc = SVC()
trained2 = clfsvc.fit(train_data, train_target)

#  testing with decision tree
predict = trained.predict(test_data)
print(predict)
# print(test_target)

# accuracy test for dsct
pct = accuracy_score(test_target, predict)
print(pct)

# testing with knn
predict1 = trained1.predict(test_data)
print(predict1)

# accuracy test for knn
acc = accuracy_score(test_target, predict1)
print(acc)

# testing with SVC
predict2 = trained2.predict(test_data)
print(predict2)

# accuracy test for SVC
acc1 = accuracy_score(test_target, predict2)
print(acc1)

# to see structure of decision tree
tree.export_graphviz(clf, out_file="tree.dot", max_depth=7, feature_names=iris.feature_names,
                     class_names=iris.target_names, filled=True, rounded=True)

# plotting graph
py.xlabel('Algorithms')
py.ylabel('Percentage')
algo = ['Dst', 'Knn', 'SVC']
accuracy_percent = [pct, acc, acc1]
py.scatter(algo, accuracy_percent, color='r', s=100, marker='o')
py.show()
