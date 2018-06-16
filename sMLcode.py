from  sklearn  import  tree


#  apple &  orange  ---   weigth,textture,color
#  texture:smooth ==  0  and  bumpy  ==  1
# color: red== 0 , green == 1, orange == 2

features=[[100,0,0], [130,0,1], [135,1,2],[150,1,2]]

output=["Red apple","Green apple","small orange","orange"]


#  now loading  decisiontree classifier

algo=tree.DecisionTreeClassifier()

#  Now training  the features and output set

trained=algo.fit(features,output)   #  generally looking for 1 core  CPU  --  [GPU ]

#  testing  trained  model  OR  Q &  A
predicted=trained.predict([[126,1,1]])

#  priting  result

print(predicted)

