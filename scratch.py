from sklearn import tree
# 0 - smooth and 1- bumpy
# the three digit numbers are weight
# 1-red , 2-green ,3- orange
data = [[100, 0, 1], [130, 0, 2], [135, 1, 3], [150, 1, 3]]
output = ['red apple', 'green apple', 'small orange', 'orange']
algo = tree.DecisionTreeClassifier()
trained_algo = algo.fit(data, output)
predict = trained_algo.predict([[100, 0, 2]])
print(predict)

